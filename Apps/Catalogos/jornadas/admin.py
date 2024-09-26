from django.contrib import admin

# Register your models here.
from Apps.Catalogos.jornadas.models import Jornada

class JornadaAdmin (admin.ModelAdmin):
    list_display = ['id_jornada', 'nombre_jornada', 'descripcion']
    search_fields = ['id_jornada', 'nombre_jornada']
admin.site.register(Jornada, JornadaAdmin)