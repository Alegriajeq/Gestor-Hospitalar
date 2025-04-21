from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_agendamentos, name='lista_agendamentos'),
    path('novo/', views.criar_agendamento, name='criar_agendamento'),
]
