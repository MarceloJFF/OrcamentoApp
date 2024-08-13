from EaseFinance.models import*

class OrcamentoSetorAno(models.Model):
    orcamento_ano = models.ForeignKey(OrcamentoAnual, null=False, on_delete= models.CASCADE)
    setor = models.ForeignKey(Setor, null = False, on_delete=models.CASCADE)
    valor_total = models.DecimalField("valor",decimal_places=5,max_digits=10,null = False)
    def __str__(self) -> str:
        return f'Valor do Orcamento do Setor  {self.valor_total}'
