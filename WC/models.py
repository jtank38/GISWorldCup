from django.db import models
from django.contrib.gis import *
from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible



class Stadiums(models.Model):
	

	class Meta:
		verbose_name_plural ='Stadiums'

	city_name = models.CharField(max_length=254,default='null')
	stadium_ca = models.BigIntegerField(default=0)
	stadiumcod = models.CharField(max_length=254,default='null')
	stadiumnam = models.CharField(max_length=254,default='null')
	latitude = models.FloatField(default=0)
	picurl=models.CharField(max_length=500,default='https://static.dezeen.com/uploads/2013/03/dezeen_Joao-Havelange-Olympic-Stadium-photo-by-Ministerio-das-Relacoes-Exteriores-Brasil_1a.jpg')
	longitude = models.FloatField(default=0)
	worldcup=models.CharField(max_length=254, default='WorldCup2014')
	geom = models.MultiPointField(srid=4326)
	
	def __str__(self):
		return self.stadiumcod.encode('utf8')



class StadClub(models.Model):
	
	class Meta:
		verbose_name_plural ='StadClubs'
	team = models.CharField(max_length=254,default='null')
	fdcouk = models.CharField(max_length=254,default='null')
	city = models.CharField(max_length=254,default='null')
	stadium = models.CharField(max_length=254,default='null')
	capacity = models.BigIntegerField(default=0)
	revenue=models.BigIntegerField(default=0)
	latitude = models.FloatField(default=0)
	picurl=models.CharField(max_length=500,default='https://static.dezeen.com/uploads/2013/03/dezeen_Joao-Havelange-Olympic-Stadium-photo-by-Ministerio-das-Relacoes-Exteriores-Brasil_1a.jpg')
	longitude = models.FloatField(default=0)
	country = models.CharField(max_length=254)
	geom = models.MultiPointField(srid=4326)




	
	def __str__(self):
		return self.team.encode('utf8')
	
	


class WCTeams(models.Model):
	
	class Meta:
		verbose_name_plural ='WCTeams'
	
	AssociationName=models.CharField(max_length=254)
	Continent=models.CharField(max_length=254)
	CountryName=models.CharField(max_length=254)
	CountryCode=models.CharField(max_length=254)

	def __str__(self):
		return self.CountryCode.encode('utf8')


class WCup(models.Model):
	
	class Meta:
		verbose_name_plural ='WCup'
	
	date=models.DateField()
	MatchName=models.CharField(max_length=254)
	MatchNumber=models.CharField(max_length=254,default='null')
	stadiumcod=models.ForeignKey(Stadiums)

	def __str__(self):
		return str(self.MatchNumber)

	# def __iter__(self):
	#     for field_name in self._meta.get_all_field_names():
	#         value = getattr(self, field_name, None)
	#         yield (field_name, value)


class WCStanding(models.Model):
	
	class Meta:
		verbose_name_plural ='WCStandings'
	
	WCGroupName=models.CharField(max_length=254)
	CountryCode=models.ForeignKey(WCTeams)
	PositionGroup=models.IntegerField(default=0)
	Points=models.IntegerField(default=0)
	GoalsAgainst=models.IntegerField(default=0)
	Played=models.IntegerField(default=0)
	Won=models.IntegerField(default=0)
	Drawn=models.IntegerField(default=0)
	Loss=models.IntegerField(default=0)
	


	def __str__(self):
		return self.WCGroupName
		


class WCMatch(models.Model):

	MatchNumber=models.ForeignKey(WCup)
	MatchLinup=models.CharField(max_length=254,default='null')
	Score=models.CharField(max_length=254)
	class Meta:
		verbose_name_plural ='WCMatches'
		

	def __str__(self):
		return self.MatchLinup


@python_2_unicode_compatible
class PlayerScore(models.Model):
	
	class Meta:
		verbose_name_plural ='PlayerScores'
	
	MatchNumber=models.ForeignKey(WCup)
	PlayerName=models.CharField(max_length=254)
	Minute=models.CharField(max_length=254)
	PlayerCountry=models.CharField(max_length=254,default='null')
	
	def __str__(self):
		return self.PlayerName





