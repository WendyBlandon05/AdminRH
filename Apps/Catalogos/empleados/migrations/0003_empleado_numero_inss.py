# Generated by Django 4.2.16 on 2024-09-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_alter_empleado_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='numero_inss',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
