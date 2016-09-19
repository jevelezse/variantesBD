import csv
from datetime import date

from gene_variants.models import Paciente
from gene_variants.models import Variante


def chunked_csv_records(csv_fn):
    csv_data = csv.reader(
        open(csv_fn),
        delimiter=',',
        strict=True,
    )

    chunk = []
    for row in csv_data:
        break  # saltar encabezado

    for row in csv_data:
        chunk.append(row)

        if len(chunk) == 1000:
            yield chunk
            chunk = []

    if len(chunk):
        yield chunk


def id_(s):
    return s


def parse_homocigoto(s):
    return s.lower() == 'hom'


# LISTA DE TODAS LAS COLUMNAS EN EL CSV
CSV_COL_NAMES = [
    ('cromosoma', id_),
    ('pos_inicio', int),
    ('pos_fin', int),
    ('ref', id_),
    ('alt', id_),
    ('funcion_gen_ref', id_),
    ('gen', id_),
    ('detalle_gen', id_),
    ('tipo_variante', id_),
    ('referencia_cambioAA', id_),
] + [  # COLUMNAS NO USADAS POR AHORA
    ('1000G_ALL', id_),
    ('1000G_AFR', id_),
    ('1000G_AMR', id_),
    ('1000G_EAS', id_),
    ('1000G_EUR', id_),
    ('1000G_SAS', id_),
    ('ExAC_Freq', id_),
    ('ExAC_AFR', id_),
    ('ExAC_AMR', id_),
    ('ExAC_EAS', id_),
    ('ExAC_FIN', id_),
    ('ExAC_NFE', id_),
    ('ExAC_OTH', id_),
    ('ExAC_SAS', id_),
    ('ESP6500si_ALL', id_),
    ('ESP6500si_AA', id_),
    ('ESP6500si_EA', id_),
    ('CG46', id_),
    ('NCI60', id_),
    ('dbSNP', id_),
    ('COSMIC_ID', id_),
    ('COSMIC_DIS', id_),
    ('ClinVar_SIG', id_),
    ('ClinVar_DIS', id_),
    ('ClinVar_STATUS', id_),
    ('ClinVar_ID', id_),
    ('ClinVar_DB', id_),
    ('ClinVar_DBID', id_),
    ('GWAS_DIS', id_),
    ('GWAS_OR', id_),
    ('GWAS_BETA', id_),
    ('GWAS_PUBMED', id_),
    ('GWAS_SNP', id_),
    ('GWAS_P', id_),
    ('SIFT_score', id_),
    ('SIFT_pred', id_),
    ('Polyphen2_HDIV_score', id_),
    ('Polyphen2_HDIV_pred', id_),
    ('Polyphen2_HVAR_score', id_),
    ('Polyphen2_HVAR_pred', id_),
    ('LRT_score', id_),
    ('LRT_pred', id_),
    ('MutationTaster_score', id_),
    ('MutationTaster_pred', id_),
    ('MutationAssessor_score', id_),
    ('MutationAssessor_pred', id_),
    ('FATHMM_score', id_),
    ('FATHMM_pred', id_),
    ('RadialSVM_score', id_),
    ('RadialSVM_pred', id_),
    ('LR_score', id_),
    ('LR_pred', id_),
    ('VEST3_score', id_),
    ('CADD_raw', id_),
    ('CADD_phred', id_),
    ('GERP++_RS', id_),
    ('phyloP46way_placental', id_),
    ('phyloP100way_vertebrate', id_),
    ('SiPhy_29way_logOdds', id_),
] + [
    ('homocigoto', parse_homocigoto),
]
# other unused columns
# Otherinfo
# Otherinfo
# Otherinfo
# Otherinfo
# Otherinfo
# Otherinfo
# Otherinfo
# Otherinfo
# Otherinfo
# Otherinfo
# Otherinfo
# Otherinfo
CSV_COL = {
    col_name: (idx, parser_func)
    for idx, (col_name, parser_func)
    in enumerate(CSV_COL_NAMES)
}


def variante_from_csvrow(row, paciente):
    v = Variante()
    v.paciente = paciente

    # LISTA DE LAS COLUMNAS QUE QUEREMOS TOMAR DEL CSV
    for col_name in [
        'cromosoma', 'pos_inicio', 'pos_fin',
        'ref', 'alt', 'gen', 'tipo_variante',
        'referencia_cambioAA', 'homocigoto',
        'funcion_gen_ref',
    ]:
        pos, parser = CSV_COL[col_name]
        setattr(v, col_name, parser(row[pos]))

    return v


def cargar_variantes(paciente, csv_fn):
    for row_chunk in chunked_csv_records(csv_fn):
        variantes = [
            variante_from_csvrow(row, paciente)
            for row in row_chunk
        ]
        Variante.objects.bulk_create(variantes)


def run():
    paciente = Paciente(
        codigo='256523',
        edad=25,
        sexo='M',
        historia_clinica='Paciente sano, nada que decir al respecto'
    )
    paciente.save()
    cargar_variantes(paciente, '../anotacion.csv')
