from django.contrib import admin

# Register your models here.
from .models import Tipo_contrato

class TipoContratoAdmin(admin.ModelAdmin):
    list_display = ['Nombre_Tipo']
    search_fields = ['Nombre_Tipo',]
admin.site.register(Tipo_contrato, TipoContratoAdmin)