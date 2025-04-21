from django.shortcuts import render

def lista_consultas(request):
    return render(request, 'consulta/lista_consultas.html')
