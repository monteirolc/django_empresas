from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.


class Documento(models.Model):
    description = models.CharField(max_length=100, verbose_name='descrição')
    belongs_to = models.ForeignKey(Funcionario, verbose_name='Pertence a',
                                   on_delete=models.PROTECT)

    def __str__(self):
        return self.description
