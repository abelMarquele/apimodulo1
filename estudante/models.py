from io import BytesIO
from PIL import Image
from django.core.validators import RegexValidator
from django.core.files import File
from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model



# Create your models here.

class Endereco(models.Model):
    provincia = models.CharField(verbose_name=('Província'),
                            max_length=30,
                            default='',
                            blank=True)
    cidade = models.CharField(verbose_name=('Cidade'),
                            max_length=30,
                            default='',
                            blank=True)
    distrito = models.CharField(verbose_name=('Distrito'),
                            max_length=30,
                            default='',
                            blank=True)
    bairro = models.CharField(verbose_name=('Bairro'),
                            max_length=30,
                            default='',
                            blank=True)
    av_rua = models.CharField(verbose_name=('Av/Rua'),
                            max_length=30,
                            default='',
                            blank=True)
    quarterao = models.CharField(verbose_name=('Nº de Quarterão'),
                            max_length=5,
                            default='',
                            blank=True)
    casa = models.CharField(verbose_name=('Nº de Casa'),
                            max_length=5,
                            default='',
                            blank=True)

    class Meta:
        ordering = ('provincia',)
    
    def __str__(self):
        return self.provincia


class Telefone(models.Model):
    tel_regex = RegexValidator(
                            regex=r'^\+?1?\d{5,15}$', 
                            message="O numero deve ter esse formato: '+999999999'")
    numero = models.CharField(validators=[tel_regex],
                            blank=True,
                            max_length=16, verbose_name='Nº telefone')  # validators should be a list

    class Meta:
        ordering = ('numero',)
    
    def __str__(self):
        return self.numero


class Encarregado(models.Model):
    nameEncarregado = models.CharField(verbose_name=('Nome do Encarregado'),
                            blank=True,
                            default='',
                            max_length=350)
    localTrabalho = models.CharField(verbose_name=('Local de Trabalho'),
                            max_length=50,
                            default='',
                            blank=True)
    Profissao = models.CharField(verbose_name=('Profissão'),
                            max_length=50,
                            default='',
                            blank=True)
    cargo = models.CharField(verbose_name=('Cargo'),
                            max_length=50,
                            default='',
                            blank=True)
    grauParentesco = models.CharField(verbose_name=('Grau de Parentesco'),
                            max_length=50,
                            default='',
                            blank=True)
    
    telefone = models.ForeignKey(Telefone, related_name="encarregadoTelefone", on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, related_name="encarregadoEndereco", on_delete=models.CASCADE)

    class Meta:
        ordering = ('nameEncarregado',)
    
    def __str__(self):
        return self.nameEncarregado



class Filiacao(models.Model):
    namePai = models.CharField(verbose_name=('Nome do Pai'),
                            blank=True,
                            default='',
                            max_length=350)
    nameMae = models.CharField(verbose_name=('Nome do Mãe'),
                            blank=True,
                            default='',
                            max_length=350)
    localTrabalhoPai = models.CharField(verbose_name=('Local de Trabalho do Pai'),
                            max_length=50,
                            default='',
                            blank=True)
    localTrabalhoMae = models.CharField(verbose_name=('Local de Trabalho da Mãe'),
                            max_length=50,
                            default='',
                            blank=True)
    ProfissaoPai = models.CharField(verbose_name=('Profissão do Pai'),
                            max_length=50,
                            default='',
                            blank=True)
    ProfissaoMae = models.CharField(verbose_name=('Profissão da Mãe'),
                            max_length=50,
                            default='',
                            blank=True)
    
    telefone = models.ForeignKey(Telefone, related_name="filiacaoTelefone", on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, related_name="filiacaoEndereco", on_delete=models.CASCADE)

    class Meta:
        ordering = ('namePai',)
    
    def __str__(self):
        return self.namePai




class Estudante(models.Model):
    nameEstudante = models.CharField(verbose_name=('Nome Completo'),
                            blank=True,
                            default='',
                            max_length=350)
    dtNascimento = models.DateField(verbose_name=('Data de nascimento'),
                            blank=True,
                            null=True)
    SEXO_CHOICES =          (('M', u'Masculino'),
                            ('F', u'Feminino'))
    sexo = models.CharField(verbose_name=('Sexo'),
                            max_length=1,
                            choices=SEXO_CHOICES)
    ESTADO_CIVIL_CHOICES = (('S', u'Solteiro'),
                            ('C', u'Casado'),
                            ('D', u'Divorciado'),
                            ('V', u'Viúvo'))
    estado_civil = models.CharField(verbose_name=('Estado civil'),
                            max_length=1,
                            default='S',
                            choices=ESTADO_CIVIL_CHOICES)
    email = models.CharField(verbose_name=('Email'),
                            blank=True,
                            default='',
                            max_length=250,
                            unique=True)
    doc = models.FileField(null=True, 
                            blank=True, 
                            upload_to='documents/',)
    ndoc = models.CharField(verbose_name=('Nº de BI/Cédula'),
                            max_length=20,
                            default='',
                            unique=True,
                            blank=True)
    dtDoc = models.DateField(verbose_name=('Data de Emissão'),
                            blank=True,
                            null=True)
    image = models.ImageField(null=True, 
                            blank=True, 
                            upload_to='upload/',)
    thumbnail = models.ImageField(upload_to='uploads/',
                            blank=True, 
                            null=True)

    telefone = models.ForeignKey(Telefone, related_name="estudanteTelefone", on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, related_name="estudanteEndereco", on_delete=models.CASCADE)
    encarregado = models.ForeignKey(Encarregado, related_name="estudanteEncarregado", on_delete=models.CASCADE)
    filiacao = models.ForeignKey(Filiacao, related_name="estudanteFiliacoe", on_delete=models.CASCADE)


    class Meta:
        ordering = ('nameEstudante',)
    
    def __str__(self):
        return self.nameEstudante

    def get_doc(self):
        if self.doc:
            return 'http://127.0.0.1:8000' + self.doc.url
        return ''

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
