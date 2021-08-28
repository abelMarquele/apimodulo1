from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import decorators
from rest_framework import permissions

from parametro.models import Sala
from parametro.models import Periodo
from parametro.models import Classe
from parametro.models import Turma

from parametro.serializers import SalaSerializer
from parametro.serializers import PeriodoSerializer
from parametro.serializers import ClasseSerializer
from parametro.serializers import TurmaSerializer

# Create your views here.

@decorators.permission_classes((permissions.AllowAny,))
class SalaViewSet(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

@decorators.permission_classes((permissions.AllowAny,))
class PeriodoViewSet(ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer

@decorators.permission_classes((permissions.AllowAny,))
class ClasseViewSet(ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

@decorators.permission_classes((permissions.AllowAny,))
class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer