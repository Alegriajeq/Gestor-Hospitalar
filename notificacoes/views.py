from django.shortcuts import render

# Create your views here.
# views.py
from django.core.mail import send_mail

def enviar_notificacao(paciente_email, assunto, mensagem):
    send_mail(assunto, mensagem, 'hospital@exemplo.com', [paciente_email])
