from models import*


class Gestor(Funcionario):
    equipe = models.ManyToManyField(Funcionario, related_name='gestores')  # Relacionamento explícito
    

