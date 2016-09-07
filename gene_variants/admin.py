from django.contrib import admin

from .models import Variante

class VarianteAdmin(admin.ModelAdmin):
    list_display = [
        'cromosoma',
        'gen',
        'pos_inicio',
        'pos_fin',
        'ref',
        'alt',
        'funcion_exonica',
        'referencia_cambio',
        'homocigoto',
        'paciente',
    ]


admin.site.register(Variante, VarianteAdmin)
