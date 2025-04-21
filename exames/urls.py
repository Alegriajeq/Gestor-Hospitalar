from django.urls import path
from .views import lista_exames, cadastrar_exame

urlpatterns = [
    path('', lista_exames, name='lista_exames'),
    path('novo/', cadastrar_exame, name='cadastrar_exame'),
]
