from audioop import reverse
from EaseFinance.models import*



class Empresa(models.Model):
    nome = models.CharField(max_length=20, help_text='Digite o nome da empresa',null = False)
    ramo = models.CharField(max_length=25, help_text='Digite o ramo da empresa',null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])