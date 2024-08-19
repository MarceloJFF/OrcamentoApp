from EaseFinance.models import*

class OrcamentoAnual(models.Model):
    valor_total = models.DecimalField("valor",decimal_places=5,max_digits=10,null = False)
    ano = models.IntegerField(null = False, unique=True)
    #status = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)