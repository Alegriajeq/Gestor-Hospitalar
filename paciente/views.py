from django.shortcuts import render, redirect
from .models import Paciente
from datetime import datetime  # Importa para tratar a data

def cadastrar_paciente(request):
    if request.method == 'POST':
        try:
            # Converte data de nascimento com validação
            data_str = request.POST.get('data_nascimento')
            try:
                data_nascimento = datetime.strptime(data_str, "%Y-%m-%d").date()
            except ValueError:
                return render(request, 'paciente/cadastrar.html', {
                    'erro': 'Data inválida. Use o formato AAAA-MM-DD.'
                })

            # Cria o paciente
            Paciente.objects.create(
                nome=request.POST.get('nome'),
                bi=request.POST.get('bi'),
                data_nascimento=data_nascimento,
                endereco=request.POST.get('endereco'),
                telefone=request.POST.get('telefone'),
                alergias=request.POST.get('alergias'),
                historico=request.POST.get('historico'),
            )
            return redirect('lista_pacientes')
        except Exception as e:
            return render(request, 'paciente/cadastrar.html', {'erro': str(e)})

    return render(request, 'paciente/cadastrar.html')


# NOVA VIEW PARA LISTAR PACIENTES
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/lista.html', {'pacientes': pacientes})
