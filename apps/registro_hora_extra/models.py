from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    reason = models.CharField(max_length=50, verbose_name='Motivo')
    worker = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, verbose_name='Funcionario')
    hours = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Horas')
    used = models.BooleanField(default=False, verbose_name='Usadas')
    def get_absolute_url(self):
        return reverse("list_overtime")
    

    def __str__(self):
        return self.reason
