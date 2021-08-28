from rest_framework import serializers
from .models import Matricula, Matricula_Turma

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
   


class Matricula_TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula_Turma
        fields = '__all__'
   

