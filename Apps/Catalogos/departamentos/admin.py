from django.contrib import admin
from .models import Departamento

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['id_departamento', 'nombre_departamento', 'descripcion', 'id_contratos']
    search_fields = ['nombre_departamento', 'descripcion']

admin.site.register(Departamento, DepartamentoAdmin)