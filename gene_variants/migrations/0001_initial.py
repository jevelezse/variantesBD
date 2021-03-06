# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=4)),
                ('madre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos_como_madre', to='gene_variants.Paciente')),
                ('padre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos_como_padre', to='gene_variants.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Variante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cromosoma', models.CharField(choices=[('chr1', 'chr1'), ('chr2', 'chr2'), ('chr3', 'chr3'), ('chr4', 'chr4'), ('chr5', 'chr5'), ('chr6', 'chr6'), ('chr7', 'chr7'), ('chr8', 'chr8'), ('chr9', 'chr9'), ('chr10', 'chr10'), ('chr11', 'chr11'), ('chr12', 'chr12'), ('chr13', 'chr13'), ('chr14', 'chr14'), ('chr15', 'chr15'), ('chr16', 'chr16'), ('chr17', 'chr17'), ('chr18', 'chr18'), ('chr19', 'chr19'), ('chr20', 'chr20'), ('chr21', 'chr21'), ('chr22', 'chr22'), ('chrX', 'chrX'), ('chrY', 'chrY')], max_length=7)),
                ('gen', models.CharField(max_length=40)),
                ('pos_inicio', models.IntegerField()),
                ('pos_fin', models.IntegerField()),
                ('ref', models.CharField(choices=[('A', 'A'), ('G', 'G'), ('T', 'T'), ('C', 'C')], max_length=1)),
                ('alt', models.CharField(choices=[('A', 'A'), ('G', 'G'), ('T', 'T'), ('C', 'C')], max_length=1)),
                ('funcion_exonica', models.CharField(choices=[('nsn', 'nonsynonymous SNV'), ('sn', 'synonymous SNV'), ('sg', 'stopgain'), ('sl', 'stoploss'), ('ukw', 'unknown')], max_length=4)),
                ('referencia_cambio', models.TextField()),
                ('homocigoto', models.BooleanField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gene_variants.Paciente')),
            ],
        ),
    ]
