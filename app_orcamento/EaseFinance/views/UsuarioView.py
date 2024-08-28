from re import template
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from EaseFinance.models import *
from EaseFinance.services.UsuarioServiceSolicitacao import UsuarioServiceSolicitacao
from EaseFinance.services.DespesaService import DespesaService
from EaseFinance.services.SolicitacaoService import SolicitacaoService
from EaseFinance.services.SetorService import SetorService


class UsuarioView():
    def index(request):
        return render(request,template_name = 'Usuario/index.html',status = 200)
    
    def realocao(request):
        return render(request,template_name = 'Usuario/realocacao.html',status = 200)
    
    def solicitacao_abono(request):
        usuario_logado = Funcionario.objects.filter(usuario = request.user).first()
        
        if(request.method == 'GET'):
            #delegar para classe de servico
            despesas = UsuarioServiceSolicitacao.obter_despesas_do_setor(usuario_logado)
            tipo_solicitacao_filtradas = [ (chave, valor) for chave, valor in TIPO_SOLICITACAO if chave in [1, 2] ]
            ultimas_solicitacoes = SolicitacaoService.obter_solicitacoes_do_usuario(usuario_logado)

            #fazer a consulta com o dia da despesa
            contexto = {'tipos_solicitacoes': tipo_solicitacao_filtradas,
                        'despesas':despesas,
                        'solicitacoes': ultimas_solicitacoes
                        } 

            return render(request,template_name = 'Usuario/solicitacao_abono.html',context=contexto,status = 200)
        
        elif(request.method == 'POST'):   
            #adicionar no repositorio e servico
            tipo_despesa = request.POST.get('categoria_despesa')
            valor_despesa = request.POST.get('valor_despesa')
            prazo_limite = request.POST.get('prazo_limite')
            motivo = request.POST.get('motivo') 
            observacao = request.POST.get('observacao')
            tipo_solicitacao = request.POST.get('categoria_solicitacao')
            
            
            tipo_despesa = DespesaService.obter_despesa(tipo_despesa)
            try:
                usuario_logado = User.objects.filter(username = request.user.username).first()
                
                nova_solicitacao = Solicitacao.objects.create(
                user = usuario_logado,
                tipo = tipo_solicitacao,
                motivo = motivo, 
                valor = valor_despesa,
                despesa = tipo_despesa ,
                prazo = prazo_limite,
                observacao = observacao)
                messages.success(request, "Solicitação criada com sucesso.")
            
            except Exception as e:
                print(e)
                messages.error(request, "Erro ao criar registro")

            
        return redirect('usuario-solicitacao-abono')
        
    def setores(request):
        
        setores_gestor = []
        
        setores = SetorService.listar_setores()
        for setor in setores:
            gestor = Gestor.objects.filter(setor=setor.id).first()
            setores_gestor.append({
                'gestor': gestor,
                'setor': setor 
            }) 
        print(setores_gestor)
        contexto = {'setores': setores_gestor}
        return render(request,template_name = 'Usuario/setores.html',context = contexto, status = 200)
        
    def perfil(request):
        return render(request,template_name = 'Usuario/perfil.html',status = 200)
    
    def sobre(request):
        return render(request,template_name = 'Usuario/sobre.html',status = 200)
    
    
    

            

