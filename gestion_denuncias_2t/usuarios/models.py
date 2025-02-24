from django.db import models
from django.contrib.auth.models import User  

# Modelo Profile que representa a los usuarios de la aplicación
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    bio = models.TextField(blank=True, null=True)  

    # Método para representar el perfil como una cadena de texto
    def __str__(self):
        return f"Profile of {self.user.username}"  
