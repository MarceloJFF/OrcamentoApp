from EaseFinance.models.Funcionario import*


class Gestor(Funcionario):
    equipe = models.ManyToManyField(Funcionario, related_name='equipe')  # Relacionamento explícito
    descricao_atividades = models.CharField(max_length=300)  
