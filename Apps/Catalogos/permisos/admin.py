from django.contrib import admin

# Register your models here.
from .models import Permiso
class PermisoAdmin(admin.ModelAdmin):
    list_display = ['nombre_permiso', 'id_empleados', 'id_tipo_permisos']
    search_fields = ['nombre_permiso', 'id_empleados__primer_nombre', 'id_empleados__numero_cedula', 'id_tipo_permisos__nombre']
admin.site.register(Permiso, PermisoAdmin)
