from django import forms
from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.image:
            self.fields['image'].help_text = f'<img src="{self.instance.image.url}" width="200" style="margin-top:10px;" />'
