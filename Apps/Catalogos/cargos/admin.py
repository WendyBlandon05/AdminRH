from django.contrib import admin

# Register your models here.
from Apps.Catalogos.cargos.models import Cargos


class CargosAdmin(admin.ModelAdmin):

   list_display = ['id_cargos', 'nombre_cargo', 'descripcion', 'salario_base', 'id_contratos']
   search_fields = ['nombre_cargo', 'id_contratos__codigo_contrato']

admin.site.register(Cargos, CargosAdmin)