# Generated by Django 4.2.16 on 2024-09-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detallepermiso', '0003_alter_detalle_permiso_fecha_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_permiso',
            name='fecha_fin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='detalle_permiso',
            name='fecha_inicio',
            field=models.DateTimeField(),
        ),
    ]
