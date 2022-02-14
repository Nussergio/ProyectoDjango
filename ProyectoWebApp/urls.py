
from django.contrib import admin
from django.urls import path, include
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('servicio', views.servicios, name='servicio'),
    path('tienda', views.tienda, name='tienda'),
    path('blog', views.blog, name='blog'),
    path('contacto', views.contacto, name='contacto'),
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)