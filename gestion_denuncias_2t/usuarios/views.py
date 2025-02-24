from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login, authenticate, logout  
from django.contrib import messages  
from .models import Profile  
from .forms import UserProfileForm, CustomUserCreationForm  
from django.contrib.auth.decorators import login_required  

# Vista para el registro de un usuario
def register(request):
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  
            login(request, user)  
            messages.success(request, 'Registro aceptado. Has iniciado sesión')  
            return redirect('profile')  
        else:
            messages.error(request, 'Ha habido un error al intentar registrarte. Prueba otra vez.') 
    else:
        form = CustomUserCreationForm()  
    
    return render(request, 'usuarios/register.html', {'form': form})  

# Vista para iniciar sesión
def login_view(request):
    if request.method == 'POST':  
        username = request.POST['username'] 
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password)  
        
        if user is not None:  
            login(request, user)  
            messages.success(request, 'Has iniciado sesión con exito.')  
            next_url = request.GET.get('next', 'profile') 
            return redirect(next_url)  
        else:
            messages.error(request, 'Nombre y contraseña invalida. Prueba otra vez.') 
    
    return render(request, 'usuarios/login.html')  

# Vista para mostrar el perfil del usuario
@login_required  
def profile(request):
    return render(request, 'usuarios/profile.html')  

# Vista para cerrar sesión
@login_required  
def logout_view(request):
    logout(request)  
    messages.success(request, 'Has cerrado sesión con exito.')  
    return redirect('login')  
