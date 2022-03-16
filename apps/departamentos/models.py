from django.db import models

# Create your models here.


class Departamento(models.Model):
    name = models.CharField(max_length=70, verbose_name='nome')

    def __str__(self):
        return self.name
