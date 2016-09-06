import csv
from datetime import date

from gene_variants.models import Paciente
from gene_variants.models import Variante


def chunked_csv_records(csv_fn):
    csv_data = csv.reader(
        open(csv_fn),
        delimiter='|',
        strict=True,
    )

    chunk = []
    for row in csv_data:
        chunk.append(row)

        if len(chunk) == 1000:
            yield chunk
            chunk = []

    if len(chunk):
        yield chunk


CSV_COL_NAMES = [
    'cromosoma',
    'pos_inicio',
    'pos_fin',
    'ref',
    'alt',
]

# Func.refgene	Gene.refgene	GeneDetail.refgene	ExonicFunc.refgene	AAChange.refgene	1000G_ALL	1000G_AFR	1000G_AMR	1000G_EAS	1000G_EUR	1000G_SAS	ExAC_Freq	ExAC_AFR	ExAC_AMR	ExAC_EAS	ExAC_FIN	ExAC_NFE	ExAC_OTH	ExAC_SAS	ESP6500si_ALL	ESP6500si_AA	ESP6500si_EA	CG46	NCI60	dbSNP	COSMIC_ID	COSMIC_DIS	ClinVar_SIG	ClinVar_DIS	ClinVar_STATUS	ClinVar_ID	ClinVar_DB	ClinVar_DBID	GWAS_DIS	GWAS_OR	GWAS_BETA	GWAS_PUBMED	GWAS_SNP	GWAS_P	SIFT_score	SIFT_pred	Polyphen2_HDIV_score	Polyphen2_HDIV_pred	Polyphen2_HVAR_score	Polyphen2_HVAR_pred	LRT_score	LRT_pred	MutationTaster_score	MutationTaster_pred	MutationAssessor_score	MutationAssessor_pred	FATHMM_score	FATHMM_pred	RadialSVM_score	RadialSVM_pred	LR_score	LR_pred	VEST3_score	CADD_raw	CADD_phred	GERP++_RS	phyloP46way_placental	phyloP100way_vertebrate	SiPhy_29way_logOdds	Otherinfo	Otherinfo	Otherinfo	Otherinfo	Otherinfo	Otherinfo	Otherinfo	Otherinfo	Otherinfo	Otherinfo	Otherinfo	Otherinfo	Otherinfo
CSV_COL = {
    (col_name, idx)
    for idx, col_name
    in enumerate(CSV_COL_NAMES)
}


def variante_from_csvrow(row, paciente):
    v = Variante()
    v.paciente = paciente

    for col_name in []:
        setattr(v, col_name, row[CSV_COL[col_name]])

    return v


def cargar_variantes(paciente, csv_fn):
    for row_chunk in chunked_csv_records(csv_fn):
        variantes = [
            variante_from_csvrow(row, paciente)
            for row in row_chunk
        ]


def run():
    paciente = Paciente(
        codigo='256523',
        fecha_nacimiento=date(1984, 04, 01),
        sexo='M',
    )
    paciente.save()
