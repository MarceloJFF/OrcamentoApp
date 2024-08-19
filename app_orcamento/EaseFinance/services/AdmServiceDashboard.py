from datetime import datetime
from EaseFinance.repository.OrcamentoAnualRepositorio import OrcamentoAnualRepositorio

class AdmServiceDashboard():
    
    def __init__(self) -> None:
        pass
    
    def obter_orcamento_ano_atual(self):
        ano_atual = datetime.now().year
        orcamento_atual = OrcamentoAnualRepositorio()
        orcamento_atual = orcamento_atual.obter_orcamento_por_ano(ano_atual)
        return orcamento_atual
