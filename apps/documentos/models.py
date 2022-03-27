from django.db import models
from apps.funcionarios.models import Funcionario
from django.urls import reverse

# Create your models here.


class Documento(models.Model):
    description = models.CharField(max_length=100, verbose_name='descrição')
    belongs_to = models.ForeignKey(Funcionario, verbose_name='pertence a',
                                   on_delete=models.PROTECT)
    file = models.FileField(upload_to='Documentos', verbose_name='arquivo')

    def get_absolute_url(self):
        return reverse("update_worker", args=[self.belongs_to.id])

    def __str__(self):
        return self.description
