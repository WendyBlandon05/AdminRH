from django.db import models
from Apps.Catalogos.contratos.models import Contrato

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    id_contratos = models.ForeignKey(Contrato, on_delete=models.CASCADE, db_column= 'id_contratos')


