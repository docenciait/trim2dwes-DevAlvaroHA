from django.urls import path  
from . import views  

# Definición de las URLs de la aplicación "denuncias"
urlpatterns = [
    path('create/', views.create_denuncia, name='create_denuncia'), 
    path('list/', views.list_denuncia, name='list_denuncia'),  
    path('update/<int:denuncia_id>/', views.update_denuncia, name='update_denuncia'),  
    path('delete/<int:denuncia_id>/', views.delete_denuncia, name='delete_denuncia'),  
]
