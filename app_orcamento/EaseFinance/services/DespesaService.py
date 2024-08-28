
from EaseFinance.repository.DespesaRepository import *

class DespesaService():
    
    def obter_despesa(id):
        return DespesaRepository.obter_despesa_por_id(id)