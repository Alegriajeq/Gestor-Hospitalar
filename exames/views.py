from django.shortcuts import render, redirect
from .models import Exame
from paciente.models import Paciente
from django.db.models import Q

def lista_exames(request):
    query = request.GET.get('q')
    exames = Exame.objects.all()

    if query:
        exames = exames.filter(
            Q(paciente__nome__icontains=query) |
            Q(tipo_exame__icontains=query)
        )

    return render(request, 'exames/lista_exames.html', {'exames': exames, 'query': query})

def cadastrar_exame(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente_id')
        tipo_exame = request.POST.get('tipo_exame')
        data_exame = request.POST.get('data_exame')

        try:
            paciente = Paciente.objects.get(id=paciente_id)
        except Paciente.DoesNotExist:
            return render(request, 'exames/cadastrar_exame.html', {
                'erro': 'Paciente não encontrado.',
                'pacientes': Paciente.objects.all()
            })

        Exame.objects.create(
            paciente=paciente,
            tipo_exame=tipo_exame,
            data_exame=data_exame
        )
        return redirect('lista_exames')

    pacientes = Paciente.objects.all()
    return render(request, 'exames/cadastrar_exame.html', {'pacientes': pacientes})
