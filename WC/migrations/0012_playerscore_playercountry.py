# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-22 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WC', '0011_stadiums_worldcup'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerscore',
            name='PlayerCountry',
            field=models.CharField(default=b'null', max_length=254),
        ),
    ]
