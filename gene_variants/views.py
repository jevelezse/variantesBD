from django.shortcuts import render

from .forms import PacienteGenForm
from .models import Variante


def paciente_gen(request):
    search_form = PacienteGenForm(request.GET)

    if not search_form.is_valid():
        return render(request, 'paciente_gen.html', dict(
            search_form=PacienteGenForm(),
        ))

    return render(request, 'paciente_gen.html', dict(
        search_form=search_form,
        variantes=Variante.objects.filter(
            paciente=search_form.cleaned_data['paciente1'],
            gen=search_form.cleaned_data['gen'],
        ),
    ))

