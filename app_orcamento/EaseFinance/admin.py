from django.contrib import admin
from EaseFinance.models import Despesa,Administrador,Funcionario,Gestor,OrcamentoAnual,OrcamentoDespesaSetor,OrcamentoSetorAno,Setor,Solicitacao
# Register your models here.
admin.site.register(Despesa)
admin.site.register(Administrador)
admin.site.register(Funcionario)
admin.site.register(Gestor)
admin.site.register(OrcamentoAnual)
admin.site.register(OrcamentoDespesaSetor)
admin.site.register(OrcamentoSetorAno)
admin.site.register(Setor)
admin.site.register(Solicitacao)