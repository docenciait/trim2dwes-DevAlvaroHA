from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Definir la vista 'home' que redirige al login
def home(request):
    return redirect('login')  # Redirige a la página de login 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  
    path('usuarios/', include('usuarios.urls')),  
    path('denuncias/', include('denuncias.urls')),  
]
