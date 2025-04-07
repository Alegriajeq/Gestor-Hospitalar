# myapp/views.py

from django.shortcuts import render, redirect
from .forms import PacienteForm  # Certifique-se de ter um formulário para cadastro

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)  # Instancia o formulário com os dados do POST
        if form.is_valid():
            form.save()  # Salva os dados no banco
            return redirect('cadastro-paciente')  # Redireciona para a página de cadastro após sucesso
    else:
        form = PacienteForm()  # Cria um formulário vazio se a requisição for GET

    return render(request, 'cadastro_paciente.html', {'form': form})  # Renderiza o template com o formulário
