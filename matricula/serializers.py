from rest_framework import serializers
from .models import Matricula, Matricula_Turma

class MatriculaSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
   


class Matricula_TurmaSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Matricula_Turma
        fields = '__all__'
   

