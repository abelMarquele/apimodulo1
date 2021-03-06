from estudante.models import Estudante
from parametro.models import Classe
from django.db import models

# Create your models here.


class Matricula(models.Model):
    numero_processo = models.CharField(verbose_name=('Número de Processo'),
                            max_length=15,
                            default='',
                            blank=True)
    ano_lectivo = models.DateField(verbose_name=('Ano Lectivo'),
                            blank=True,
                            null=True)
    CONFERIDO_CHOICES =     (('S', u'Sim'),
                            ('N', u'Não'))
    conferido = models.CharField(verbose_name=('Status da matrícula (se foi validada ou não)'),
                            max_length=1,
                            choices=CONFERIDO_CHOICES)

    estudante = models.ForeignKey(Estudante, related_name="matriculaEstudante", on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, related_name="matriculaClasse", on_delete=models.CASCADE)

    class Meta:
        ordering = ('numero_processo',)
    
    def __str__(self):
        return self.numero_processo

class Matricula_Turma(models.Model):
    matricula = models.ForeignKey(Estudante, related_name="matricula_turmaMatricula", on_delete=models.CASCADE)
    turma = models.ForeignKey(Classe, related_name="matricula_turmaTurma", on_delete=models.CASCADE)