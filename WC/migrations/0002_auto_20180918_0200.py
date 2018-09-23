# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-18 02:00
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WC', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stadiums',
            name='Latitude',
        ),
        migrations.RemoveField(
            model_name='stadiums',
            name='StadiumCode',
        ),
        migrations.RemoveField(
            model_name='stadiums',
            name='StadiumName',
        ),
        migrations.AddField(
            model_name='stadiums',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPointField(default=0, srid=4326),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='stadiumnam',
            field=models.CharField(default=b'null', max_length=254),
        ),
    ]