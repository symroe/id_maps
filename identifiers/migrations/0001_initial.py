# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=500)),
                ('namespace', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationship', to='identifiers.Identifier')),
                ('same_as', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='same_as', to='identifiers.Identifier')),
            ],
        ),
    ]