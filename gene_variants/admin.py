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

    search_fields = ['^gen']


    def get_search_results(self, request, queryset, search_term):
        all_entries = self.model.objects.all() 
        search_term = search_term.strip()
        if len(search_term) >= 1:
            all_entries = all_entries.filter(gen__startswith=search_term)

        for k,v in request.GET.items():
            filterargs = {k:v}
            if k.startswith('homocigoto') or k.startswith('paciente') or k.startswith('clinvar_sig') or k.startswith('tipo_variante') :
                all_entries = all_entries.filter(**filterargs) 
        return (all_entries, False)

    list_filter = ['paciente','tipo_variante','homocigoto', 'clinvar_sig']
    search_fields = ['paciente']

    


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

    search_fields = ['historia_clinica']

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Variante, VarianteAdmin)
