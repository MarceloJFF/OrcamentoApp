


from EaseFinance.models import *


class OrcamentoDespesaSetorRepository():
    
    def obter_despesas_do_setor(usuario_logado):
         despesas_setor_usuario = OrcamentoDespesaSetor.objects.filter(setor = usuario_logado.setor).all()
         return despesas_setor_usuario