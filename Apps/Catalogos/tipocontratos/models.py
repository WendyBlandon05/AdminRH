from django.db import models

# Create your models here.
class Tipo_contrato(models.Model):
    id_tipo_contratos = models.AutoField(primary_key=True)
    Nombre_Tipo = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.id_tipo_contratos}"