#!/bin/bash

$1

python manage.py runscript load_variants --traceback --script-args ~/Escritorio/$1.csv ~/Escritorio/$1

mv ~/Escritorio/$1.csv ~/Escritorio/hechos
mv ~/Escritorio/$1 ~/Escritorio/hechos