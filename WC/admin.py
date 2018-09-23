# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class StadiumsAdmin(LeafletGeoAdmin):
	list_display=['city_name','stadium_ca','stadiumcod','stadiumnam','latitude','picurl','longitude','worldcup','geom']

class StadClubAdmin(LeafletGeoAdmin):
	list_display=['team','fdcouk','city','stadium','capacity','revenue','latitude','picurl','longitude','country','geom']

class WCTeamsAdmin(admin.ModelAdmin):
	list_display=['AssociationName','Continent','CountryName','CountryCode']

class WCupAdmin(admin.ModelAdmin):
	list_display=['date','MatchName','MatchNumber','stadiumcod']

class WCStandingAdmin(admin.ModelAdmin):
	list_display=['WCGroupName','CountryCode','PositionGroup','Points','GoalsAgainst','Played','Won','Drawn','Loss','PositionGroup']

class WCMatchAdmin(admin.ModelAdmin):
	list_display=['MatchNumber','MatchLinup','Score']

class PlayerScoreAdmin(admin.ModelAdmin):
	list_display=['MatchNumber','PlayerName','Minute','PlayerCountry']



admin.site.register(Stadiums,StadiumsAdmin)
admin.site.register(WCTeams,WCTeamsAdmin)
admin.site.register(WCup,WCupAdmin)
admin.site.register(WCStanding,WCStandingAdmin)
admin.site.register(WCMatch,WCMatchAdmin)
admin.site.register(PlayerScore,PlayerScoreAdmin)
admin.site.register(StadClub,StadClubAdmin)



