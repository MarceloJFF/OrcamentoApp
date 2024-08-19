
from EaseFinance.models.OrcamentoAnual import OrcamentoAnual


class OrcamentoAnualRepositorio():
    def obter_orcamento_por_ano(self,ano):
        orcamento_anual = None
        if( ano is not None and ano != " "):
            orcamento_anual =  OrcamentoAnual.objects.filter(ano = ano).first()
        return orcamento_anual