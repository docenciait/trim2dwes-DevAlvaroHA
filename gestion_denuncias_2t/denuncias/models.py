from django.db import models  
from django.contrib.auth.models import User  

# Modelo Device que representa los dispositivos de la aplicación
class Denuncia(models.Model):
    titulo = models.CharField(max_length=100)  
    descripcion = models.TextField(max_length=250) 
    categoria = models.CharField(max_length=100)  
    status = models.CharField(max_length=100) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    # Método para representar el dispositivo como una cadena de texto
    def __str__(self):
        return f"{self.name} ({self.type})"  
