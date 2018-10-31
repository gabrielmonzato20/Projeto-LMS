from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def aluno(request):
    return render(request, 'aluno.html')

def disciplina(request):
    return render(request, 'disciplina.html')

def professor(request):
    return render(request, 'professor.html')

