# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-18 02:03
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WC', '0002_auto_20180918_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadiums',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
        ),
    ]
