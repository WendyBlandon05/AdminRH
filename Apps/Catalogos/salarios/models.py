from django.db import models
from Apps.Catalogos.contratos.models import Contrato

from Apps.Catalogos.nominas.models import Nomina
# Create your models here.
class Salario(models.Model):
    id_salario = models.AutoField(primary_key=True)
    id_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    horas_trabajadas = models.IntegerField()
    pago_hora = models.DecimalField(max_digits=8, decimal_places=2)
    salario_neto = models.DecimalField(max_digits=10, decimal_places=2)
    salario_bruto = models.DecimalField(max_digits=10, decimal_places=2)

    id_nomina = models.ForeignKey(Nomina, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.id_contrato}"