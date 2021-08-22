from django.urls import path, include
from django.urls.resolvers import URLPattern

from estudante import views

urlpatterns = [
    path('latest-estudantes/', views.LastEstudanteList.as_view()),
]