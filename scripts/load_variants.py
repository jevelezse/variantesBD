import csv
from collections import namedtuple
from datetime import date
from os import path

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
	return (s.lower() == 'hom')


def parse_clinvar_sig(s):
    s = s.strip()
    if s == ".":
        return ""
    unique_cvsigs = set(s.split("|"))

    if 'other' in unique_cvsigs and len(unique_cvsigs) > 1:
        unique_cvsigs.discard('other')

    return "|".join(sorted(unique_cvsigs))


RefCambio = namedtuple('RefCambio', [
    'gen', 'num_acceso', 'exon', 'camb_nucl', 'camb_AA',
])
def parse_referencia_cambio(s):
    refs_s = s.split(",")
    try:
        refs = [RefCambio(*(ref_s.split(":"))) for ref_s in refs_s]
    except TypeError:
        return s
    unique_refs = dict()
    for ref in refs:
        unique_refs[(ref.gen, ref.exon, ref.camb_nucl, ref.camb_AA)] = ref

    refs_s = [
        "{0.gen}:{0.exon}:{0.camb_nucl}:{0.camb_AA}".format(unique_refs[k])
        for k in sorted(unique_refs)
    ]
    return "\n".join(refs_s)


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
    ('referencia_cambioAA', parse_referencia_cambio),
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
    ('clinvar_sig', parse_clinvar_sig),
    ('ClinVar_DIS', id_),
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
    ('SIFT_converted_rankscore', id_),
    ('SIFT_pred', id_),
    ('Polyphen2_HDIV_score', id_),
    ('Polyphen2_HDIV_rankscore', id_),
    ('Polyphen2_HDIV_pred', id_),
    ('Polyphen2_HVAR_score', id_),
    ('Polyphen2_HVAR_rankscore', id_),
    ('Polyphen2_HVAR_pred', id_),
    ('LRT_score', id_),
    ('LRT_converted_rankscore', id_),
    ('LRT_pred', id_),
    ('MutationTaster_score', id_),
    ('MutationTaster_converted_rankscore', id_),
    ('MutationTaster_pred', id_),
    ('MutationAssessor_score', id_),
    ('MutationAssessor_score_rankscore', id_),
    ('MutationAssessor_pred', id_),
    ('FATHMM_score', id_),
    ('FATHMM_converted_rankscore', id_),
    ('FATHMM_pred', id_),
    ('PROVEAN_score', id_),
    ('PROVEAN_converted_rankscore', id_),
    ('PROVEAN_pred', id_),
    ('VEST3_score', id_),
    ('VEST3_rankscore', id_),
    ('MetaSVM_score', id_),
    ('MetaSVM_rankscore', id_),
    ('MetaSVM_pred', id_),
    ('MetaLR_score', id_),
    ('MetaLR_rankscore', id_),
    ('MetaLR_pred', id_),
    ('M-CAP_score', id_),
    ('M-CAP_rankscore', id_),
    ('M-CAP_pred', id_),
    ('CADD_raw', id_),
    ('CADD_raw_rankscore', id_),
    ('CADD_phred', id_),
    ('DANN_score', id_),
    ('DANN_rankscore', id_),
    ('fathmm-MKL_coding_score', id_),
    ('fathmm-MKL_coding_rankscore', id_),
    ('fathmm-MKL_coding_pred', id_),
    ('Eigen_coding_or_noncoding', id_),
    ('Eigen-raw', id_),
    ('Eigen-PC-raw', id_),
    ('GenoCanyon_score', id_),
    ('GenoCanyon_score_rankscore', id_),
    ('integrated_fitCons_score', id_),
    ('integrated_fitCons_score_rankscore', id_),
    ('integrated_confidence_value', id_),
    ('GERP++_RS', id_),
    ('GERP++_RS_rankscore', id_),
    ('phyloP100way_vertebrate', id_),
    ('phyloP100way_vertebrate_rankscore', id_),
    ('phyloP20way_mammalian', id_),
    ('phyloP20way_mammalian_rankscore', id_),
    ('phastCons100way_vertebrate', id_),
    ('phastCons100way_vertebrate_rankscore', id_),
    ('phastCons20way_mammalian', id_),
    ('phastCons20way_mammalian_rankscore', id_),
    ('SiPhy_29way_logOdds', id_),
    ('SiPhy_29way_logOdds_rankscore', id_),
    ('Interpro_domain', id_),
    ('GTEx_V6_gene', id_),
    ('GTEx_V6_tissue', id_),
    ('gnomAD_exome_ALL', id_),
    ('gnomAD_exome_AFR', id_),
    ('gnomAD_exome_AMR', id_),
    ('gnomAD_exome_ASJ', id_),
    ('gnomAD_exome_EAS', id_),
    ('gnomAD_exome_FIN', id_),
    ('gnomAD_exome_NFE', id_),
    ('gnomAD_exome_OTH', id_),
    ('gnomAD_exome_SAS', id_),
    ('gnomAD_genome_ALL', id_),
    ('gnomAD_genome_AFR', id_),
    ('gnomAD_genome_AMR', id_),
    ('gnomAD_genome_ASJ', id_),
    ('gnomAD_genome_EAS', id_),
    ('gnomAD_genome_FIN', id_),
    ('gnomAD_genome_NFE', id_),
    ('gnomAD_genome_OTH', id_),
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
        'funcion_gen_ref', 'clinvar_sig',
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


def cargar_datos_paciente(archivo_datos_paciente):
    codigo = path.basename(archivo_datos_paciente)
    with open(archivo_datos_paciente) as datos_paciente:
        linea_edad = datos_paciente.readline().strip()
        edad = int(linea_edad.split()[-1])

        linea_sexo = datos_paciente.readline().strip()
        sexo = linea_sexo.split()[-1]

        historia_clinica = datos_paciente.read()

    return (codigo, edad, sexo, historia_clinica)


def run(csv_variantes, archivo_datos_paciente):
    codigo, edad, sexo, historia_clinica = cargar_datos_paciente(archivo_datos_paciente)

    paciente = Paciente(
        codigo=codigo,
        edad=edad,
        sexo=sexo,
        historia_clinica=historia_clinica,
    )
    paciente.save()
    cargar_variantes(paciente, csv_variantes)
