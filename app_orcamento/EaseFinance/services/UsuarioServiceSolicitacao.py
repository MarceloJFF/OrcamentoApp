


from EaseFinance.repository.OrcamentoDespesaSetorRepository import OrcamentoDespesaSetorRepository


class UsuarioServiceSolicitacao():
    def __init__(self) -> None:
        pass
    
    def obter_despesas_do_setor(usuario_logado):
        despesas = OrcamentoDespesaSetorRepository.obter_despesas_do_setor(usuario_logado)
        return despesas