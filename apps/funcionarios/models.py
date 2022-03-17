from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

# Create your models here.


class Funcionario(models.Model):
    name = models.CharField(max_length=100, verbose_name='nome')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departaments = models.ManyToManyField(
        Departamento, verbose_name='departamentos')
    company = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, verbose_name='Empresa',
        null=True, blank=True)

    def __str__(self):
        return self.name
