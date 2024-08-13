from models import*

class OrcamentoAnual(models.Model):
    empresa = models.OneToOneField(Empresa, help_text="Escolha a empresa vinculada",null = False, on_delete=models.CASCADE)
    valor_total = models.models.DecimalField("valor",decimal_places=5,null = False)
    ano = models.models.models.IntegerField(("ano"),max_digits=5,null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    