from django.shortcuts import render
from django.http import HttpResponse

# Esse metodo trara na tela ola mundo para o caminho 172.0.0.0:8000
'''
def inicio(request):
    return HttpResponse('Olá, Mundo')
'''

def inicio(request):
    return render(request, 'inicio.html')

# Create your views here.
