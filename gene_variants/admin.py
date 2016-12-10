from django.contrib import admin

from .models import Variante
from .models import Paciente

class VarianteAdmin(admin.ModelAdmin):
    list_display = [
        'paciente',
        'cromosoma',
        'gen',
        'pos_inicio',
        'pos_fin',
        'ref',
        'alt',
        'tipo_variante',
        'funcion_gen_ref',
        'homocigoto_str',
        'referencia_cambioAA',
    ]

    list_filter = ['paciente', 'homocigoto', 'gen']



class PacienteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'padre',
        'madre',
        'codigo',
        'edad',
        'sexo',
        'historia_clinica',
    ]

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Variante, VarianteAdmin)
