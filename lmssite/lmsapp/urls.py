from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('aluno/', aluno, name='aluno'),
    path('disciplina/', disciplina, name='disciplina'),
    path('professor/', professor, name='professor'),
]
