from django.contrib import admin

# Register your models here.
from Apps.Catalogos.nominas.models import Nomina

class NominaAdmin(admin.ModelAdmin):
    list_display = ['id_nomina', 'mes_pagado', 'total_pagar', 'fecha_pago']
    search_fields = ['id_nomina','fecha_pago']

admin.site.register(Nomina, NominaAdmin)