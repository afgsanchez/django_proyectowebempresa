from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Post
from .forms import PostAdminForm  # Importas el formulario que creamos

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
