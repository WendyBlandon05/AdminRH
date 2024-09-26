from django.db import models
from Apps.Catalogos.salarios.models import Salario

# Create your models here.
class Deducciones(models.Model):
    id_deducciones = models.AutoField(primary_key=True)
    id_salario = models.ForeignKey(Salario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    monto = models.DecimalField(max_digits=10, decimal_places=2)