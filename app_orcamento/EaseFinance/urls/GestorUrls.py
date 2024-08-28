from django.urls import path
from EaseFinance.views.UsuarioView import UsuarioView
from EaseFinance.views.GestorView import GestorView

urlpatterns = [
    path("solicitacoes", GestorView.index, name='solicitacoes')
]
