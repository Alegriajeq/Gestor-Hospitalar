from django.shortcuts import render

def lista_notificacoes(request):
    return render(request, 'notificacoes/lista.html')  # ou o nome do template correto

