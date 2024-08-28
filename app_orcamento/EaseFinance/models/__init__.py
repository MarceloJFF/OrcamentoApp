from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


TIPO_SOLICITACAO = (
    (1,'Compras de Produtos ou equipamentos'),
    (2, 'Despesas em Geral'),
    (3, 'Realocao do Orcamento Interno das Despesas no Setor'),
    (4, 'Transferencia de Valores de  Orcamento entre Setores')
)

from .Despesa import Despesa
from.Setor import Setor
from.OrcamentoAnual import OrcamentoAnual
from.OrcamentoDespesaSetor import OrcamentoDespesaSetor
from.OrcamentoSetorAno import OrcamentoSetorAno
from.Solicitacao import Solicitacao
from.Funcionario import Funcionario
from.Gestor import Gestor
from.Administrador import Administrador