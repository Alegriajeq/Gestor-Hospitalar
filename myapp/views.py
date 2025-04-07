
from django.shortcuts import render, redirect
from .forms import PacienteForm

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_paciente')
    else:
        form = PacienteForm()
    return render(request, 'cadastro_paciente.html', {'form': form})
