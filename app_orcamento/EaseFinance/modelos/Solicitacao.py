
from modelos import*

class Solicitacao(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=False)
    tipo = models.IntegerField(choices=TIPO_SOLICITACAO, default=1, null=False)
    motivo = models.CharField(null=False, max_length=100)
    status = models.BooleanField(default=False)
    valor = models.DecimalField(decimal_places=5,null=False)
    observacao = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f'{self.tipo}  {self.motivo}'
    
