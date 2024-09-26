from symtable import Class

from django.contrib import admin

# Register your models here.
from Apps.Catalogos.beneficios.models import Beneficios

class BeneficiosAdmin(admin.ModelAdmin):
    list_display = ['id_beneficios', 'nombre_beneficio', 'monto', ]
    search_fields = ['id_beneficios', 'nombre_beneficio', 'id_empleado__numero_cedula']


admin.site.register(Beneficios, BeneficiosAdmin)