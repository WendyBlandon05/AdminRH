from django.db import models

# Create your models here.
class Nomina(models.Model):
    id_nomina = models.AutoField(primary_key=True)
    mes_pagado = models.CharField(max_length= 20)
    total_pagar = models.DecimalField(max_digits=20, decimal_places=2)
    fecha_pago = models.DateField()