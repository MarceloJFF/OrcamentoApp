from EaseFinance.models.Despesa import Despesa

class DespesaRepository:

    def obter_despesa_por_id(self,id):
        despesa = None
        if( id is not None and id != " "):
            despesa =  Despesa.objects.filter(id = id).first()
        return despesa
    
    def obter_despesa_por_nome(self,nome):
        despesa = None
        if( nome is not None and nome != " "):
            despesa =  Despesa.objects.filter(nome = nome).first()
        return despesa
    
    def obter_todas_despesas(self):
        return Despesa.objects.all()
    
    def criar_despesa(self, nome, descricao):
        return Despesa.objects.create(
            nome = nome,
            descricao = descricao
        )
    
    def deletar_despesa(self, id):
        despesa = self.obter_despesa_por_id(id)
        if despesa is not None:
            despesa.delete()
        return despesa
    