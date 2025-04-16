# myApp/views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  # ou qualquer outro template que você deseja renderizar

