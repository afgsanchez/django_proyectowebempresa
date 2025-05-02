from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Inicio - Home Page</h1>")
    return render(request, "core/home.html")

def about(request):
    # return HttpResponse("Historia - About Page")
    return render(request, "core/about.html")

def store(request):
    # return HttpResponse("Visítanos - Store Page")
    return render(request, "core/store.html")
