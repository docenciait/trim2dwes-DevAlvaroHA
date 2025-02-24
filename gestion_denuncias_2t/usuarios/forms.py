from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from .models import Profile  

# Formulario de creación de usuario personalizado
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  
    bio = forms.CharField(widget=forms.Textarea, required=False)  

    class Meta:
        model = User  
        fields = ['username', 'email', 'password1', 'password2']  

    def save(self, commit=True):
        user = super().save(commit=False)  
        if commit:
            user.save()  
            profile = Profile.objects.create(user=user)  
            profile.email = self.cleaned_data.get('email') 
            profile.save() 
        return user 

# Formulario para editar el perfil del usuario
class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)  
    username = forms.CharField(max_length=100, required=True)  
    bio = forms.CharField(widget=forms.Textarea, required=False)  

    class Meta:
        model = User  
        fields = ['username', 'email']  

    def save(self, commit=True):
        user = super().save(commit=False)  
        if commit:
            user.save()  
            profile = Profile.objects.get(user=user)  
            profile.bio = self.cleaned_data.get('bio')  
            profile.save()  
        return user  
