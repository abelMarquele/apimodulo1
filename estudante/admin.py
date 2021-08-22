from django.contrib import admin

from .models import Estudante, Encarregado, Endereco, Filiacao, Telefone

# Register your models here.

admin.site.register(Estudante)
admin.site.register(Encarregado)
admin.site.register(Endereco)
admin.site.register(Filiacao)
admin.site.register(Telefone)

