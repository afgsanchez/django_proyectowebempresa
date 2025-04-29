from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    # return HttpResponse("Servicios - Services Page")
    services = Service.objects.all()
    return render(request, "services/services.html", {'services':services})