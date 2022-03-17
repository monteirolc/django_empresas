from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.


class RegistroHoraExtra(models.Model):
    reason = models.CharField(max_length=50, verbose_name='motivo')
    worker = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, verbose_name='Funcionario')

    def __str__(self):
        return self.reason
