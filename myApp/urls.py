from django.contrib import admin
from django.urls import path, include  # <- INCLUIR ISSO
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home_redirect'),
    path('paciente/', include('paciente.urls')) ,
    path('medicos/', include('medicos.urls')),
    path('agendamentos/', include('agendamento.urls')),
    path('exames/', include('exames.urls')), 
    path('consultas/', include('consulta.urls')),
    path('notificacoes/', include('notificacoes.urls')), 


]
