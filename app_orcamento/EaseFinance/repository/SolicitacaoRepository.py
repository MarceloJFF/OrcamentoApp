from EaseFinance.models.Solicitacao import Solicitacao

class SolicitacaoRepository():

    def obter_solicitacao_por_id(self,id):
        solicitacao = None
        if( id is not None and id != " "):
            solicitacao =  Solicitacao.objects.filter(id = id).first()
        return solicitacao
    
    def obter_todas_solicitacoes(self):
        return Solicitacao.objects.all()
    
    def atualizar_solicitacao(self, id, **kwargs):
        solicitacao = self.obter_solicitacao_por_id(id)
        if solicitacao is not None:
            for key, value in kwargs.items():
                setattr(solicitacao, key, value)
            solicitacao.save()
        return solicitacao
    
    def deletar_solicitacao(self, id):
        solicitacao = self.obter_solicitacao_por_id(id)
        if solicitacao is not None:
            solicitacao.delete()
        return solicitacao
    
    def criar_solicitacao(self, user, tipo, motivo, valor, observacao):
        return Solicitacao.objects.create(
            user = user,
            tipo = tipo,
            motivo = motivo,
            valor = valor,
            observacao = observacao
        )