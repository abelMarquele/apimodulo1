from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import decorators
from rest_framework import permissions

from matricula.models import Matricula
from matricula.models import Matricula_Turma

from matricula.serializers import MatriculaSerializer
from matricula.serializers import Matricula_TurmaSerializer

# Create your views here.

@decorators.permission_classes((permissions.AllowAny,))
class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

@decorators.permission_classes((permissions.AllowAny,))
class Matricula_TurmaViewSet(ModelViewSet):
    queryset = Matricula_Turma.objects.all()
    serializer_class = Matricula_TurmaSerializer
