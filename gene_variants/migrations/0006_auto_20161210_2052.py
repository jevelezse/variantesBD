# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-10 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gene_variants', '0005_auto_20160912_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='variante',
            name='clinvar_sig',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='madre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos_como_madre', to='gene_variants.Paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos_como_padre', to='gene_variants.Paciente'),
        ),
    ]