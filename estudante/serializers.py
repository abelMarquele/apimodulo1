from rest_framework import serializers
from .models import Estudante, Encarregado, Endereco, Filiacao, Telefone


class EstudanteSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'
   




class EnderecoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
   




class EncarregadoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Encarregado
        fields = '__all__'




class FiliacaoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Filiacao
        fields = '__all__'




class TelefoneSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'

    
    

