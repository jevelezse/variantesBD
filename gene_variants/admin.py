from django.contrib import admin

from .models import Variante
from .models import Paciente

class VarianteAdmin(admin.ModelAdmin):
    list_display = [
        'cromosoma',
        'gen',
        'pos_inicio',
        'pos_fin',
        'ref',
        'alt',
        'tipo_variante',
        'funcion_gen_ref',
        'referencia_cambioAA',
        'homocigoto',
        'paciente',

    ]

class PacienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Variante, VarianteAdmin)
