from django.contrib import admin

# Register your models here.
from .models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['numero_cedula', 'numero_inss','primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'sexo', 'telefono', 'email']
    search_fields = ['numero_cedula', 'primer_nombre', 'primer_apellido', 'email']

admin.site.register(Empleado, EmpleadoAdmin)