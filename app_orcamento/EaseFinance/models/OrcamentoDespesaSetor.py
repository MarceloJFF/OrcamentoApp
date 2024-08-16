from EaseFinance.models import*

class OrcamentoDespesaSetor(models.Model): 
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null = False, related_name='setor')
    despesa = models.ForeignKey( Despesa ,on_delete=models.CASCADE,null = False,related_name='despesa')
    valor = models.DecimalField(max_digits=10, decimal_places=5,null = False)
    def __str__(self):
        return f'Orcamento setor despesa {self.valor}'
