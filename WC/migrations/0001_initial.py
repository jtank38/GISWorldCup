# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PlayerName', models.CharField(max_length=25)),
                ('Minute', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'PlayerScores',
            },
        ),
        migrations.CreateModel(
            name='Stadiums',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StadiumName', models.CharField(max_length=50)),
                ('StadiumCode', models.CharField(max_length=15)),
                ('Latitude', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True)),
            ],
            options={
                'verbose_name_plural': 'Stadiums',
            },
        ),
        migrations.CreateModel(
            name='WCMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MatchLinup', models.CharField(default=b'null', max_length=25)),
                ('Score', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'WCMatches',
            },
        ),
        migrations.CreateModel(
            name='WCStanding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('WCGroupName', models.CharField(max_length=15)),
                ('Points', models.IntegerField(default=0)),
                ('GoalsAgainst', models.IntegerField(default=0)),
                ('Played', models.IntegerField(default=0)),
                ('Won', models.IntegerField(default=0)),
                ('Drawn', models.IntegerField(default=0)),
                ('Loss', models.IntegerField(default=0)),
                ('PositionGroup', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'WCStandings',
            },
        ),
        migrations.CreateModel(
            name='WCTeams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AssociationName', models.CharField(max_length=4)),
                ('Continent', models.CharField(max_length=15)),
                ('CountryName', models.CharField(max_length=20)),
                ('CountryCode', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name_plural': 'WCTeams',
            },
        ),
        migrations.CreateModel(
            name='WCup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('MatchName', models.CharField(max_length=15)),
                ('MatchNumber', models.IntegerField(default=0, max_length=3)),
                ('StadiumCode', models.ForeignKey(to='WC.Stadiums')),
            ],
            options={
                'verbose_name_plural': 'WCup',
            },
        ),
        migrations.AddField(
            model_name='wcstanding',
            name='CountryCode',
            field=models.ForeignKey(to='WC.WCTeams'),
        ),
        migrations.AddField(
            model_name='wcmatch',
            name='MatchNumber',
            field=models.ForeignKey(to='WC.WCup'),
        ),
        migrations.AddField(
            model_name='playerscore',
            name='MatchNumber',
            field=models.ForeignKey(to='WC.WCup'),
        ),
    ]
