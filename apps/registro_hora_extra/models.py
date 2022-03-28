from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.


class RegistroHoraExtra(models.Model):
    reason = models.CharField(max_length=50, verbose_name='Motivo')
    worker = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, verbose_name='Funcionario')
    hours = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Horas')

    def __str__(self):
        return self.reason
