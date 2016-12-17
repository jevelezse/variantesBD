from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Variante
from .models import Paciente

class VarianteAdmin(admin.ModelAdmin): #filtros 
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
        'clinvar_sig',
        'html_referencia_cambioAA',
    ]

    list_filter = ['paciente', 'homocigoto', 'gen', 'clinvar_sig']

    def html_referencia_cambioAA(self, obj):
        return mark_safe(obj.referencia_cambioAA.replace("\n", "<br/>"))
    html_referencia_cambioAA.short_description = "ref. cambio"




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
