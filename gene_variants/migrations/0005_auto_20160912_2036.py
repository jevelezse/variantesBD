# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gene_variants', '0004_auto_20160912_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='fecha_nacimiento',
        ),
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='historia_clinica',
            field=models.TextField(blank=True),
        ),
    ]
