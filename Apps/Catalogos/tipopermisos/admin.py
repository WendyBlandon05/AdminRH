from django.contrib import admin

# Register your models here.
from .models import Tipo_permiso

class TipoPermisoAdmin(admin.ModelAdmin):
    list_display = ['id_tipo_permisos', 'nombre',]
    search_fields = ['nombre',]

admin.site.register(Tipo_permiso, TipoPermisoAdmin)
