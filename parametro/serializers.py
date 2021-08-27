from rest_framework import serializers
from .models import Sala, Periodo, Classe, Turma

class SalaSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'
   


class PeriodoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class ClasseSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'
   


class TurmaSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
   

