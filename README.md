# Cómo cargar variantes

    python manage.py runscript load_variants --traceback --script-args ../variantes.csv FBH234 34 M

El primer argumento es el archivo CSV con las variantes (en este ejemplo
`../variantes.csv`), y luego van el código del paciente (`FHB234`), la edad del
paciente (debe ser un número), y el sexo (debe ser `M` o `F`).

