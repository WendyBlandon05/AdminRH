from django.contrib import admin

# Register your models here.

from .models import Contrato

class ContratoAdmin(admin.ModelAdmin):
    list_display = ['id_contratos','codigo_contrato', 'fecha_inicio', 'fecha_conclusion', 'id_tipo_contratos', 'id_empleado']
    search_fields = ['codigo_contrato', 'id_empleado__numero_cedula', 'id_tipo_contratos__Nombre_Tipo']


admin.site.register(Contrato, ContratoAdmin)
