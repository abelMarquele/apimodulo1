from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import decorators
from rest_framework import permissions

from estudante.models import Estudante
from estudante.models import Endereco
from estudante.models import Encarregado
from estudante.models import Filiacao
from estudante.models import Telefone

from estudante.serializers import EstudanteSerializer
from estudante.serializers import EnderecoSerializer
from estudante.serializers import EncarregadoSerializer
from estudante.serializers import FiliacaoSerializer
from estudante.serializers import TelefoneSerializer

# Create your views here.

@decorators.permission_classes((permissions.AllowAny,))
class EstudanteViewSet(ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

@decorators.permission_classes((permissions.AllowAny,))
class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

@decorators.permission_classes((permissions.AllowAny,))
class EncarregadoViewSet(ModelViewSet):
    queryset = Encarregado.objects.all()
    serializer_class = EncarregadoSerializer

@decorators.permission_classes((permissions.AllowAny,))
class FiliacaoViewSet(ModelViewSet):
    queryset = Filiacao.objects.all()
    serializer_class = FiliacaoSerializer

@decorators.permission_classes((permissions.AllowAny,))
class TelefoneViewSet(ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer