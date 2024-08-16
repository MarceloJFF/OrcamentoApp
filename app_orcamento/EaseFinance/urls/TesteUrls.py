
from EaseFinance.views.TesteView import TesteView
from django.urls import path

urlpatterns = [
    path("",TesteView.renderizar)
]
