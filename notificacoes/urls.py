from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notificacoes, name='lista_notificacoes'),
]
