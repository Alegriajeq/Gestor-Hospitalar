# atendimento/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_paciente, name='cadastro-paciente'),  # Rota para a página inicial
    path('cadastrar/', views.cadastrar_paciente, name='cadastro-paciente'),  # Ou uma rota específica para cadastro
]
