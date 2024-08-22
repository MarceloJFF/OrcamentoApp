from datetime import datetime
from EaseFinance.repository.OrcamentoRepository import OrcamentoRepository

class AdmServiceDashboard():
    
    def __init__(self) -> None:
        pass
    
    def obter_orcamento_ano_atual(self):
        ano_atual = datetime.now().year
        orcamento_atual = OrcamentoRepository()
        orcamento_atual = orcamento_atual.obter_orcamento_por_ano(ano_atual)
        return orcamento_atual
