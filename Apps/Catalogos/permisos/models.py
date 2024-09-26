from tkinter.constants import CASCADE


from django.db import models
from Apps.Catalogos.empleados.models import Empleado
from Apps.Catalogos.tipopermisos.models import Tipo_permiso


# Create your models here.
class Permiso(models.Model):
    id_permisos = models.AutoField(primary_key=True)
    id_empleados = models.ForeignKey(Empleado, on_delete= models.CASCADE, db_column= 'id_empleados')
    nombre_permiso = models.CharField(max_length= 50)
    id_tipo_permisos = models.ForeignKey(Tipo_permiso, on_delete= models.CASCADE, db_column= 'id_tipo_permisos')

    def __str__(self):
        return f"{self.id_permisos}"