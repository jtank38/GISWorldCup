# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-20 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WC', '0010_auto_20180920_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadiums',
            name='worldcup',
            field=models.CharField(default=b'WorldCup2014', max_length=254),
        ),
    ]
