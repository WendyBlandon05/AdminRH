# Generated by Django 4.2.16 on 2024-09-18 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0002_contrato_fecha_conclusion_contrato_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fecha_conclusion',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha_inicio',
            field=models.DateTimeField(),
        ),
    ]
