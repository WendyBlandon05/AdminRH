from django.db import models
from Apps.Catalogos.empleados.models import Empleado
from Apps.Catalogos.tipodocumentos.models import Tipo_documento

# Create your models here.
class documentos_personales(models.Model):
    id_documentos_personales = models.AutoField(primary_key = True)
    direccion_archivo = models.CharField(max_length=100)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    id_empleados = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column= 'id_empleados')
    id_tipo_documentos = models.ForeignKey(Tipo_documento, on_delete=models.CASCADE, db_column= 'id_tipo_documentos')