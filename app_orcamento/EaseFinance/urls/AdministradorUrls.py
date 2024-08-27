
from EaseFinance.views.TesteView import TesteView
from django.urls import path
from EaseFinance.views.AdministradorView import AdministradorView

urlpatterns = [
    path("adm", AdministradorView.index, name='adm-dash'),
    path("adm/setores", AdministradorView.setores, name='adm-setores')
]
