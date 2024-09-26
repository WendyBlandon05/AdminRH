# Generated by Django 4.2.16 on 2024-09-25 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nominas', '0001_initial'),
        ('contratos', '0004_contrato_id_jornada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id_salario', models.AutoField(primary_key=True, serialize=False)),
                ('horas_trabajadas', models.IntegerField()),
                ('pago_hora', models.DecimalField(decimal_places=2, max_digits=8)),
                ('salario_neto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salario_bruto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.contrato')),
                ('id_nomina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nominas.nomina')),
            ],
        ),
    ]
