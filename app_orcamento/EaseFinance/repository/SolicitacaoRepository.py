
from EaseFinance.models.Solicitacao import Solicitacao

class SolicitacaoRepository():
    def listar_solicitacoes_usuario(usuario):
        solicitacoes = Solicitacao.objects.filter(user = usuario.id).all().order_by('-created_at')
        return solicitacoes