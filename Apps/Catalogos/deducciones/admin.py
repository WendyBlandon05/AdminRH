from django.contrib import admin

# Register your models here.
from Apps.Catalogos.deducciones.models import Deducciones

class DeduccionesAdmin(admin.ModelAdmin):
    list_display = ['id_deducciones', 'id_salario', 'descripcion', 'monto']
    search_fields = ['id_deducciones', 'descripcion']


admin.site.register(Deducciones, DeduccionesAdmin)