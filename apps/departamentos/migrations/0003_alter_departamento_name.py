# Generated by Django 4.0.3 on 2022-03-20 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_departamento_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=70, unique=True, verbose_name='nome'),
        ),
    ]
