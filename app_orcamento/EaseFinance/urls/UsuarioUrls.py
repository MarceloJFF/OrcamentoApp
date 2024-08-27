from django.urls import path
from EaseFinance.views.UsuarioView import UsuarioView

urlpatterns = [
    path("", UsuarioView.index, name='usuario-dash'),
    path("setores", UsuarioView.setores, name='usuario-setores'),
    path("realocacao", UsuarioView.realocao, name='usuario-realocacao'),
    path("solicitacao_abono", UsuarioView.solicitacao_abono, name='usuario-solicitacao-abono'),
    path("perfil", UsuarioView.perfil, name='usuario-perfil'),
    path("sobre", UsuarioView.sobre, name='usuario-sobre')

]
