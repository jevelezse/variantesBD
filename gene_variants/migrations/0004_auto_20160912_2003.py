# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gene_variants', '0003_auto_20160905_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variante',
            old_name='referencia_cambio',
            new_name='referencia_cambioAA',
        ),
        migrations.RemoveField(
            model_name='variante',
            name='funcion_exonica',
        ),
        migrations.AddField(
            model_name='variante',
            name='funcion_gen_ref',
            field=models.CharField(default='-', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variante',
            name='tipo_variante',
            field=models.CharField(default='-', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variante',
            name='alt',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='variante',
            name='ref',
            field=models.CharField(max_length=100),
        ),
    ]
