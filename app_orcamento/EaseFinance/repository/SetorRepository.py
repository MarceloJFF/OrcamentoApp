


from EaseFinance.models.Setor import Setor


class SetorRepository():
    def listar_setores():
        return Setor.objects.all()