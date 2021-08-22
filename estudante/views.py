from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Estudante, Endereco, Encarregado, Filiacao, Telefone 
from .serializers import EstudanteSerealizer,EnderecoSerealizer,EncarregadoSerealizer,FiliacaoSerealizer,TelefoneSerealizer


# Create your views here.
class LastEstudanteList(APIView):
    def get(self, request, format=None):
        estudante = Estudante.objects.all()[0:4]
        serializer = EstudanteSerealizer(estudante, many=True)
        return Response(serializer.data)