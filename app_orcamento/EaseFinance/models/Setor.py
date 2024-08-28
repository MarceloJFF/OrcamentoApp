from EaseFinance.models import*


class Setor(models.Model):
    nome = models.CharField(max_length=20, help_text = 'Digite o nome do setor', unique=True)
    telefone = models.CharField(max_length= 20, help_text ='Digite o contato do setor', null=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.nome
    
