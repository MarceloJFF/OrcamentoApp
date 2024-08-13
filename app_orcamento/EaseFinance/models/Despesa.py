from models import*

class Despesa(models.Model):
    nome = models.CharField(max_length=25,null=False, help_text='Digite o nome da despesa', unique=True,max_lenngth = 20)
    descricao = models.TextField(help_text="Digite a descrição da despesa",null=False)
    
    def __str__(self) -> str:
        return self.nome
  
    