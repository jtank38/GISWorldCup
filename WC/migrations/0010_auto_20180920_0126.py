# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-20 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WC', '0009_stadclub'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadclub',
            name='picurl',
            field=models.CharField(default=b'https://static.dezeen.com/uploads/2013/03/dezeen_Joao-Havelange-Olympic-Stadium-photo-by-Ministerio-das-Relacoes-Exteriores-Brasil_1a.jpg', max_length=500),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='picurl',
            field=models.CharField(default=b'https://static.dezeen.com/uploads/2013/03/dezeen_Joao-Havelange-Olympic-Stadium-photo-by-Ministerio-das-Relacoes-Exteriores-Brasil_1a.jpg', max_length=500),
        ),
    ]
