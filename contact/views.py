from django.shortcuts import render

# Create your views here.
def contact(request):
    # return HttpResponse("Contacto - Contact Page")
    return render(request, "contact/contact.html")