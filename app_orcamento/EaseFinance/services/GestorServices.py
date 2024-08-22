from  EaseFinance.repository.SolicitacaoRepository import SolicitacaoRepository
from  EaseFinance.repository.OrcamentoRepository import OrcamentoRepository

class GestoServices:

    def __init__(self):
        self.solicitacao = SolicitacaoRepository()
        self.orcamento = OrcamentoRepository()

    def analisar_solicitacao(self, id, status, comentario):
        solicitacao = self.solicitacao.obter_solicitacao_por_id(id)
