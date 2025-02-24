from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages  
from .models import Denuncia
from .forms import DenunciaForm  
from django.contrib.auth.decorators import login_required 

# Vista para crear una nueva denuncia
@login_required  
def create_denuncia(request):
    if request.method == 'POST':  
        form = DenunciaForm(request.POST)  
        if form.is_valid():  
            denuncia = form.save(commit=False)  
            denuncia.user = request.user 
            denuncia.save() 
            messages.success(request, 'Denuncia creada.')  
            return redirect('list_denuncia')  
        else:
            messages.error(request, 'Error al crear la denuncia. Prueba otra vez.')  
    else:
        form = DenunciaForm()  
    return render(request, 'denuncias/create_denuncia.html', {'form': form}) 

# Vista para listar todas las denuncias
@login_required  
def list_denuncia(request):
    denuncias = Denuncia.objects.all()  
    return render(request, 'denuncias/list_denuncia.html', {'denuncias': denuncias}) 

# Vista para actualizar una denuncia
@login_required  
def update_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Denuncia, id=denuncia_id)  
    if request.method == 'POST': 
        form = DenunciaForm(request.POST, instance=denuncia)  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Denuncia actualizada.')  
            return redirect('list_denuncia') 
        else:
            messages.error(request, 'Error al actualizar denuncia. Prueba otra vez.')  
    else:
        form = DenunciaForm(instance=denuncia)  
    return render(request, 'denuncias/update_denuncia.html', {'form': form})  

# Vista para eliminar una denuncia
@login_required  
def delete_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Denuncia, id=denuncia_id)  
    if request.method == 'POST':  
        denuncia.delete()  
        messages.success(request, 'Denuncia eliminada.')  
        return redirect('list_denuncia')  
    return render(request, 'denuncias/delete_denuncia.html', {'denuncia': denuncia})  
