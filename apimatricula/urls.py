from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.urls.conf import path

# Third party modules
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

# My Viewsets
from estudante.views import EstudanteViewSet
from estudante.views import EncarregadoViewSet
from estudante.views import EnderecoViewSet
from estudante.views import FiliacaoViewSet
from estudante.views import TelefoneViewSet

from matricula.views import MatriculaViewSet
from matricula.views import Matricula_TurmaViewSet


from parametro.views import SalaViewSet
from parametro.views import ClasseViewSet
from parametro.views import PeriodoViewSet
from parametro.views import TurmaViewSet

from questionario.views import Historico_SaudeViewSet
from questionario.views import PerguntaViewSet
from questionario.views import Quintil_RiquezaViewSet


admin.autodiscover()

API_TITLE = 'Modulo 1 API'
API_DESCRIPTION = 'Modulo Matrícula.'
schema_view = get_schema_view(title=API_TITLE)

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'estudante', EstudanteViewSet)
router.register(r'encarregado', EncarregadoViewSet)
router.register(r'filiacao', FiliacaoViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'telefone', TelefoneViewSet)

router.register(r'matricula', MatriculaViewSet)
router.register(r'matricula_turma', Matricula_TurmaViewSet)

router.register(r'sala', SalaViewSet)
router.register(r'classe', ClasseViewSet)
router.register(r'periodo', PeriodoViewSet)
router.register(r'turma', TurmaViewSet)

router.register(r'pergunta', PerguntaViewSet)
router.register(r'historico_Saude', Historico_SaudeViewSet)
router.register(r'quintil_riqueza', Quintil_RiquezaViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^schema/$', schema_view),
    url(r'^api/accounts/', include('authemail.urls')),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
