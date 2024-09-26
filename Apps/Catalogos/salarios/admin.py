from django.contrib import admin

# Register your models here.
from Apps.Catalogos.salarios.models import Salario

class SalarioAdmin(admin.ModelAdmin):
    list_display = ['id_salario', 'id_contrato', 'horas_trabajadas', 'pago_hora', 'salario_neto', 'salario_bruto', 'id_nomina']
    search_fields = ['id_contrato__id_empleado']

admin.site.register(Salario, SalarioAdmin)