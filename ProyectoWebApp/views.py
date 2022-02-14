from urllib import request
from django.shortcuts import render 
from Servicios.models import servicio

# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")

def servicios(request):
    
    servi = servicio.objects.all()
    
    return render(request, "ProyectoWebApp/servicio.html",{'servi': servi} )

def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")

