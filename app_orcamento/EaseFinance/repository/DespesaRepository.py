from EaseFinance.models import *
class DespesaRepository():
    
    def obter_despesa_por_id(tipo_despesa):
        tipo_despesa = Despesa.objects.filter(id = tipo_despesa).first()
        return tipo_despesa