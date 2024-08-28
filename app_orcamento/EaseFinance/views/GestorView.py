


from django.shortcuts import render

from EaseFinance.models import Gestor
from EaseFinance.models.Solicitacao import Solicitacao
from EaseFinance.services.SetorService import SetorService
from EaseFinance.models import Funcionario


class GestorView():
     def index(request):
         #quero pegar o setor do usuario logado, depois procurar as solicitacoes de usuario desse setor
         usuario_logado = Gestor.objects.filter(usuario = request.user).first()
         
         funcionarios = Funcionario.objects.all()
         solicitacoes_setor = []        
         setores = SetorService.listar_setores()
         for funcionario in funcionarios:
               solicitacao = Solicitacao.objects.filter(user=funcionario.usuario).filter(user__funcionario__setor = usuario_logado.setor).first()
               solicitacoes_setor.append(solicitacao)
        
            
         contexto = {'solicitacoes':solicitacoes_setor}
         return render(request,template_name = 'Gestor/tela_abono.html', context=contexto,status = 200)