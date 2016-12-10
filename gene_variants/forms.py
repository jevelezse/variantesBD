from django import forms

from  .models import Paciente
from  .models import Variante

class PacienteGenForm(forms.Form):
    paciente1 = forms.ModelChoiceField(
        label='Primer Paciente',
        queryset=Paciente.objects.all(),
    )
    paciente2 = forms.ModelChoiceField(
        label='Segundo Paciente',
        queryset=Paciente.objects.all(),
    )
    gen = forms.ChoiceField(
        label='Gen',
        choices=[],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["gen"].choices = [(None, '-----')] + [
            (gen, gen)
            for gen in Variante.objects.values_list(
                'gen', flat=True,
            ).distinct().order_by('gen')
        ]
