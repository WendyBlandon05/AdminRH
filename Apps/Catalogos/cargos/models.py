from django.db import models
from Apps.Catalogos.contratos.models import Contrato

class Cargos(models.Model):
    id_cargos = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=255, null=True)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    id_contratos = models.ForeignKey(Contrato, on_delete=models.CASCADE, db_column= 'id_contratos')

    def __str__(self):
        return self.nombre_cargo