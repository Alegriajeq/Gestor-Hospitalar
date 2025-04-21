from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),  # essa linha redireciona para a lista
    path('lista/', views.lista_pacientes, name='lista_pacientes'),
    path('cadastrar/', views.cadastrar_paciente, name='cadastrar_paciente'),
]

