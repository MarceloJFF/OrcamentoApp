

from EaseFinance.repository.SolicitacaoRepository import SolicitacaoRepository

class SolicitacaoService():
    def obter_solicitacoes_do_usuario(usuario):
        solicitacoes = SolicitacaoRepository.listar_solicitacoes_usuario(usuario)
        return solicitacoes       