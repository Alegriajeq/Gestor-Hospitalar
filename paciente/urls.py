from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_paciente, name='cadastrar_paciente'),
]
