# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identifiers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifier',
            name='code',
            field=models.CharField(blank=True, db_index=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='identifier',
            name='namespace',
            field=models.CharField(blank=True, db_index=True, max_length=500),
        ),
    ]
