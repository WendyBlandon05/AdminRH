# Generated by Django 4.2.16 on 2024-09-17 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargos',
            name='descripcion',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
