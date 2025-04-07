from django.shortcuts import render, redirect
from .forms import PacienteForm  # Certifique-se de que o formulário foi criado nesse caminho

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro-paciente')  # Nome da rota configurada no urls.py
    else:
        form = PacienteForm()

    return render(request, 'index.html', {'form': form})
