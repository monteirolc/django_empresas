from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.db.models import Sum
# Create your models here.


class Funcionario(models.Model):
    name = models.CharField(max_length=100, verbose_name='nome')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departaments = models.ManyToManyField(
        Departamento, verbose_name='departamentos')
    company = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, verbose_name='Empresa',
        null=True, blank=True)

    @property
    def total_overtime(self):
        return self.registrohoraextra_set.all().aggregate(
            Sum('hours'))['hours__sum']

    def get_absolute_url(self):
        return reverse("list_worker")

    def __str__(self):
        return self.name