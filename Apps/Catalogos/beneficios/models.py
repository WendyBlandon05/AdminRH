from django.db import models

from Apps.Catalogos.empleados.models import Empleado
from Apps.Catalogos.salarios.models import Salario


# Create your models here.
class Beneficios(models.Model):
    id_beneficios = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, on_delete= models.CASCADE)
    nombre_beneficio = models.CharField(max_length=50)
    id_salario = models.ForeignKey(Salario, on_delete= models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)