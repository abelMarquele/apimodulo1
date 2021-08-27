from django.db import models

# Create your models here.

class Pergunta(models.Model):
    codigo_pergunta  = models.CharField(verbose_name=('código'),
                            max_length=30,
                            default='',
                            blank=True)
    pergunta = models.CharField(verbose_name=('Pergunta'),
                            max_length=500,
                            default='',
                            blank=True)


    class Meta:
        ordering = ('codigo',)
    
    def __str__(self):
        return self.codigo


class Quintil_Riqueza(models.Model):
    codigo_pergunta = models.ForeignKey(Pergunta, related_name="codigoPergunta", on_delete=models.CASCADE)
    resposta = models.CharField(verbose_name=('Resposta'),
                            max_length=10,
                            default='',
                            blank=True)


    class Meta:
        ordering = ('codigo_pergunta',)
    
    def __str__(self):
        return self.codigo_pergunta

class historico_saude(models.Model):
    codigo_pergunta = models.ForeignKey(Pergunta, related_name="codigoPergunta", on_delete=models.CASCADE)
    resposta = models.CharField(verbose_name=('Resposta'),
                            max_length=10,
                            default='',
                            blank=True)


    class Meta:
        ordering = ('codigo_pergunta',)
    
    def __str__(self):
        return self.codigo_pergunta