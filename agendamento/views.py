from django.shortcuts import render, redirect
from .forms import AgendamentoForm
from .models import Agendamento

def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamentos/form.html', {'form': form})

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos/lista.html', {'agendamentos': agendamentos})
