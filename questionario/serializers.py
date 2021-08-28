from rest_framework import serializers
from .models import Pergunta, Quintil_Riqueza, historico_Saude

class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = '__all__'
   


class Quintil_RiquezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quintil_Riqueza
        fields = '__all__'

class historico_SaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = historico_Saude
        fields = '__all__'
   