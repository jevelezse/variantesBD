from django.db import models

CROMOSOMAS = [
    ('chr1', 'chr1'),
    ('chr2', 'chr2'),
    ('chr3', 'chr3'),
    ('chr4', 'chr4'),
    ('chr5', 'chr5'),
    ('chr6', 'chr6'),
    ('chr7', 'chr7'),
    ('chr8', 'chr8'),
    ('chr9', 'chr9'),
    ('chr10', 'chr10'),
    ('chr11', 'chr11'),
    ('chr12', 'chr12'),
    ('chr13', 'chr13'),
    ('chr14', 'chr14'),
    ('chr15', 'chr15'),
    ('chr16', 'chr16'),
    ('chr17', 'chr17'),
    ('chr18', 'chr18'),
    ('chr19', 'chr19'),
    ('chr20', 'chr20'),
    ('chr21', 'chr21'),
    ('chr22', 'chr22'),
    ('chrX', 'chrX'),
    ('chrY', 'chrY'),
]

SEXOS = [
    ('F', 'Femenino'),
    ('M', 'Masculino'),
]


class Paciente(models.Model):
    padre = models.ForeignKey('self', null=True, related_name='hijos_como_padre')
    madre = models.ForeignKey('self', null=True, related_name='hijos_como_madre')

    codigo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=4, choices=SEXOS)

    def __str__(self):
        return 'Paciente {} - {}'.format(self.codigo, self.sexo)


class Variante(models.Model):
    cromosoma = models.CharField(max_length=7, choices=CROMOSOMAS)
    gen = models.CharField(max_length=40)

    pos_inicio = models.IntegerField()
    pos_fin = models.IntegerField()
    ref = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    tipo_variante = models.CharField(max_length=50)

    funcion_gen_ref = models.CharField(max_length=50)

    referencia_cambioAA = models.TextField()

    homocigoto = models.BooleanField()

    paciente = models.ForeignKey('Paciente')

