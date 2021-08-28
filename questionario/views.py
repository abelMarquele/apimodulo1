from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import decorators
from rest_framework import permissions

from questionario.models import Pergunta
from questionario.models import Quintil_Riqueza
from questionario.models import historico_Saude

from questionario.serializers import PerguntaSerializer
from questionario.serializers import Quintil_RiquezaSerializer
from questionario.serializers import historico_SaudeSerializer

# Create your views here.

@decorators.permission_classes((permissions.AllowAny,))
class PerguntaViewSet(ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

@decorators.permission_classes((permissions.AllowAny,))
class Quintil_RiquezaViewSet(ModelViewSet):
    queryset = Quintil_Riqueza.objects.all()
    serializer_class = Quintil_RiquezaSerializer

@decorators.permission_classes((permissions.AllowAny,))
class historico_SaudeViewSet(ModelViewSet):
    queryset = historico_Saude.objects.all()
    serializer_class = historico_SaudeSerializer
