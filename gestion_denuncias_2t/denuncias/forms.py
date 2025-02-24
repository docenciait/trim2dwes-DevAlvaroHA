from django import forms  
from .models import Denuncia  

# Formulario para el modelo Denuncia, que permite crear y actualizar denuncias
class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia  
        fields = ['titulo', 'descripcion', 'categoria', 'status', 'user']  
