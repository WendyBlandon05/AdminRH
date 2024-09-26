from django.contrib import admin

# Register your models here.
from .models import documentos_personales

class DocumentosPersonalesAdmin(admin.ModelAdmin):
    list_display = ['direccion_archivo', 'fecha_subida', 'id_empleados', 'id_tipo_documentos']
    search_fields = ['direccion_archivo', 'id_empleados__primer_nombre', 'id_tipo_documentos__nombre']

admin.site.register(documentos_personales, DocumentosPersonalesAdmin)