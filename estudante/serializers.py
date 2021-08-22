from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Estudante, Encarregado, Endereco, Filiacao, Telefone


class EstudanteSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'
        # fields = (
        #     "nameEstudante",
        #     "dtNascimento",
        #     "sexo",
        #     "estado_civil",
        #     "email",
        #     "doc",
        #     "ndoc",
        #     "dtDoc",
        #     "image",
        #     "thumbnail",

        #     "telefone",
        #     "endereco",
        #     "encarregado",
        #     "filiacao"
        # )
    

    




class EnderecoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
        # fields = (
        #         "provincia",
        #         "cidade",
        #         "distrito",
        #         "bairro",
        #         "av_rua",
        #         "quarterao",
        #         "casa"
        # )
    




class EncarregadoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Encarregado
        fields = '__all__'
        # fields = (
        #         "nameEncarregado",
        #         "localTrabalho",
        #         "Profissao",
        #         "cargo",
        #         "grauParentesco",
    
        #         "telefone",
        #         "endereco"
        # )
   





class FiliacaoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Filiacao
        fields = '__all__'




class TelefoneSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'

    
    

