from django.db import models
from django.urls import reverse
from apps.empresas.models import Empresa
# Create your models here.


class Departamento(models.Model):
    name = models.CharField(max_length=70, verbose_name='nome')
    company = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, verbose_name='empresa')

    def get_absolute_url(self):
        return reverse("list_departament")

    def __str__(self):
        return self.name
