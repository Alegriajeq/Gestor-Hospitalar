from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Medico
from .forms import MedicoForm

def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/lista.html', {'medicos': medicos})

def novo_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico cadastrado com sucesso!')
            return redirect('lista_medicos')
    else:
        form = MedicoForm()
    return render(request, 'medicos/form.html', {'form': form, 'titulo': 'Novo Médico'})

def editar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    form = MedicoForm(request.POST or None, instance=medico)
    if form.is_valid():
        form.save()
        messages.success(request, 'Médico atualizado com sucesso!')
        return redirect('lista_medicos')
    return render(request, 'medicos/form.html', {'form': form, 'titulo': 'Editar Médico'})

def deletar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    if request.method == 'POST':
        medico.delete()
        messages.success(request, 'Médico excluído com sucesso!')
        return redirect('lista_medicos')
    return render(request, 'medicos/confirmar_exclusao.html', {'medico': medico})
