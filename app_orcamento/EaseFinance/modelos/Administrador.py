from modelos import*



class Administrador(Funcionario):
    data_promocao = models.DateField()  # Data da promoção para administrador
    descricao_atividades = models.CharField(max_length=300)  
