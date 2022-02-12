
from django.contrib import admin
from django.urls import path, include
from ProyectoWebApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('servicio', views.servicio, name='servicio'),
    path('tienda', views.tienda, name='tienda'),
    path('blog', views.blog, name='blog'),
    path('contacto', views.contacto, name='contacto'),
]
    