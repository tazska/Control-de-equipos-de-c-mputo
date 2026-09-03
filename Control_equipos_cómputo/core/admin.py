from django.contrib import admin
from .models import Equipo


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('codigo_interno', 'tipo_equipo', 'marca', 'serial', 'ubicacion', 'estado', 'fecha_registro')
    list_filter = ('tipo_equipo', 'estado', 'marca')
    search_fields = ('codigo_interno', 'marca', 'serial', 'ubicacion')
