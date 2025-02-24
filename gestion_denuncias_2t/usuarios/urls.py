from django.urls import path  
from . import views  

# Definición de las URLs de la aplicación 'usuarios'
urlpatterns = [
    path('register/', views.register, name='register'),  
    path('login/', views.login_view, name='login'),  
    path('profile/', views.profile, name='profile'),   
    path('logout/', views.logout_view, name='logout'),  
]
