from typing import Any
from models import*


class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.models.CharField(max_length=50,help_text = "Digite o seu nome", null=False)  
    sobrenome = models.models.CharField(max_length=50,help_text = "Digite o seu nome", null=False)
    setor = models.ForeignKey(Setor,on_delete=models.SET_NULL)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    data_nascimento = models.DateField(null = True,default=None)
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=20, null=False)
    
    def __str__(self) -> str:
        return f'{self.nome}  {self.sobrenome}'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Perfil.objects.create(user=instance)
        except:
            pass
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass