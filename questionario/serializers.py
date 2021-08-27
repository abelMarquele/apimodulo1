from rest_framework import serializers
from .models import Pergunta, Quintil_Riqueza, historico_Saude

class PerguntaSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = '__all__'
   


class Quintil_RiquezaSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Quintil_Riqueza
        fields = '__all__'

class historico_SaudeSerealizer(serializers.ModelSerializer):
    class Meta:
        model = historico_Saude
        fields = '__all__'
   