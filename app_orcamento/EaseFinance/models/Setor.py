from EaseFinance.models import*


class Setor(models.Model):
    nome = models.CharField(max_length=20, help_text='Digite o nome do setor', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    empresa_setor = models.ManyToManyField(Empresa,help_text="Selecione a empresa correspondente ao Setor")
    def __str__(self):
        return self.nome
    
