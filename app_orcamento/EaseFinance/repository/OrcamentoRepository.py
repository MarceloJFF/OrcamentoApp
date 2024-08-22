from EaseFinance.models import OrcamentoAnual, OrcamentoDespesaSetor, OrcamentoSetorAno

class OrcamentoRepository:

    def obter_orcamento_por_ano(self,ano):
        orcamento_anual = None
        if( ano is not None and ano != " "):
            orcamento_anual =  OrcamentoAnual.objects.filter(ano = ano).first()
        return orcamento_anual
    
    def obter_orcamento_anual_por_setor(self,ano,setor):
        orcamento_anual = self.obter_orcamento_por_ano(ano)
        orcamento_setor = None
        if( orcamento_anual is not None and setor is not None and setor != " "):
            orcamento_setor =  OrcamentoSetorAno.objects.filter(orcamento_anual = orcamento_anual, setor = setor).first()
        return orcamento_setor
    
    def obter_orcamento_despesa_setor(self, setor):
        orcamento_despesa_setor = None
        if( setor is not None and setor != " "):
            orcamento_despesa_setor =  OrcamentoDespesaSetor.objects.filter(setor = setor).all()
        return orcamento_despesa_setor
    
    def atualizar_orcamento_anual(self, ano, **kwargs):
        orcamento_anual = self.obter_orcamento_por_ano(ano)
        if orcamento_anual is not None:
            for key, value in kwargs.items():
                setattr(orcamento_anual, key, value)
            orcamento_anual.save()
        return orcamento_anual
    
    def atualizar_orcamento_setor(self, ano, setor, **kwargs):
        orcamento_setor = self.obter_orcamento_anual_por_setor(ano,setor)
        if orcamento_setor is not None:
            for key, value in kwargs.items():
                setattr(orcamento_setor, key, value)
            orcamento_setor.save()
        return orcamento_setor
    
    def atualizar_orcamento_despesa_setor(self, setor, **kwargs):
        orcamento_despesa_setor = self.obter_orcamento_despesa_setor(setor)
        if orcamento_despesa_setor is not None:
            for key, value in kwargs.items():
                setattr(orcamento_despesa_setor, key, value)
            orcamento_despesa_setor.save()
        return orcamento_despesa_setor
    
    def deletar_orcamento_anual(self, ano):
        orcamento_anual = self.obter_orcamento_por_ano(ano)
        if orcamento_anual is not None:
            orcamento_anual.delete()
        return orcamento_anual
    
    def deletar_orcamento_setor(self, ano, setor):
        orcamento_setor = self.obter_orcamento_anual_por_setor(ano,setor)
        if orcamento_setor is not None:
            orcamento_setor.delete()
        return orcamento_setor
    
    def deletar_orcamento_despesa_setor(self, setor):
        orcamento_despesa_setor = self.obter_orcamento_despesa_setor(setor)
        if orcamento_despesa_setor is not None:
            orcamento_despesa_setor.delete()
        return orcamento_despesa_setor
    
    def criar_orcamento_anual(self, ano, valor_total):
        return OrcamentoAnual.objects.create(
            ano = ano,
            valor_total = valor_total
        )
    
    def criar_orcamento_setor(self, ano, setor, valor_total):
        orcamento_anual = self.obter_orcamento_por_ano(ano)
        return OrcamentoSetorAno.objects.create(
            orcamento_anual = orcamento_anual,
            setor = setor,
            valor_total = valor_total
        )
    
    def criar_orcamento_despesa_setor(self, setor, valor_total, despesa):
        return OrcamentoDespesaSetor.objects.create(
            setor = setor,
            despesa = despesa,
            valor_total = valor_total
        )