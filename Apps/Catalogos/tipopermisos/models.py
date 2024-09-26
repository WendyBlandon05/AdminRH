from django.db import models

# Create your models here.
class Tipo_permiso(models.Model):
    id_tipo_permisos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id_tipo_permisos)