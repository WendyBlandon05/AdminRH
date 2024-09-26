from django.contrib import admin
# Register your models here.
from .models import Detalle_permiso

class DetallePermisoAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'fecha_inicio', 'fecha_fin', 'id_empleados', 'id_permisos']
    search_fields = ['descripcion', 'id_empleados__primer_nombre', 'id_permisos__nombre_permiso']

admin.site.register(Detalle_permiso, DetallePermisoAdmin)