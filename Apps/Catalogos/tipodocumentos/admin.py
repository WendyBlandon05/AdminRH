from django.contrib import admin

# Register your models here.
from .models import Tipo_documento

class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ['id_tipo_documentos', 'nombre',]
    search_fields = ['nombre',]

admin.site.register(Tipo_documento, TipoDocumentoAdmin)