from re import template
from django.http import HttpResponse
from django.shortcuts import redirect, render

from EaseFinance.models import *


class UsuarioView():
    def index(request):
        return render(request,template_name = 'Usuario/index.html',status = 200)
    
    def realocao(request):
        return render(request,template_name = 'Usuario/realocacao.html',status = 200)
    
    def solicitacao_abono(request):
        usuario_logado = Funcionario.objects.filter(usuario = request.user).first()
        
        orcamento_despesa_setor_usuario = OrcamentoDespesaSetor.objects.filter(setor = usuario_logado.setor)
        print(orcamento_despesa_setor_usuario.first().despesa.descricao)
        
        if(request.method == 'GET'):
            #delegar para classe de servico
            tipo_solicitacao_filtradas = [ (chave, valor) for chave, valor in TIPO_SOLICITACAO if chave in [2, 3] ]
            contexto = {'tipos_solicitacoes': tipo_solicitacao_filtradas} 
            return render(request,template_name = 'Usuario/solicitacao_abono.html',context=contexto,status = 200)
        elif(request.method == 'POST'):   
            #adicionar no repositorio e servico
            tipo_despesa = request.POST.get('tipo_despesa')
            valor_despesa = request.POST.get('valor_despesa')
            prazo_limite = request.POST.get('prazo_limite')
            motivo = request.POST.get('motivo') 
            observacao = request.POST.get('observacao')
            msg = " "
            _type =" "
            try:
                usuario_logado = Funcionario.objects.filter(user = request.user).first()
                nova_solicitacao = Solicitacao.objects.create(
                    user = usuario_logado,
                    tipo = tipo_despesa.id,
                    motivo = motivo, 
                    valor = valor_despesa,
                    prazo = prazo_limite,
                    observacao = observacao)
                msg = "Solicitacao Criada com Sucesso"
                _type ="Sucess"
            except:
                msg = "Erro ao criar Solicitacao. Tente novamente"
                _type = "Danger"     
            contexto = {'msg': msg, 'type': _type}
            return redirect(to="usuario-solicitacao-abono")
            

            
    def setores(request):
        return render(request,template_name = 'Usuario/setores.html',status = 200)
    
    def perfil(request):
        return render(request,template_name = 'Usuario/perfil.html',status = 200)
    
    def sobre(request):
        return render(request,template_name = 'Usuario/sobre.html',status = 200)
    
    
    

            

