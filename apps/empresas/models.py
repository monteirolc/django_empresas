from django.db import models

# Create your models here.


class Empresas(models.Model):
    name = models.CharField(
        max_length=100, help_text='Nome da Empresa', verbose_name='Nome')
