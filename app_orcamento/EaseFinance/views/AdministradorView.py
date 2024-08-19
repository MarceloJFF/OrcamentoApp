from django.http import HttpResponse
from django.shortcuts import render
from EaseFinance.services.AdmServiceDashboard import AdmServiceDashboard


class AdministradorView():
    def index(request):
        orcamento_ano_atual  = AdmServiceDashboard().obter_orcamento_ano_atual()
        contexto = {
            'orcamento_atual': orcamento_ano_atual
        }
        return render(request,template_name = 'Administrador/dashboard.html',context=contexto ,status = 200)
    
    #def setores(request):
        #return render(request,template_name = 'Administrador/setores.html', status = 200)
    def setores(request):
        return render(request,template_name = 'Administrador/setores.html', status = 200)

