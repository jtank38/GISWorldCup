import csv
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from .models import *



path='/home/jubanjan/WCGIS/WC/CSVFiles/wc2018'
os.chdir(path)

#Mapping For  Model "WCTeams"

# from .models import WCTeams
# #path='/home/jubanjan/WCGIS/WC/CSVFiles'
# #os.chdir(path)
# def run():
# 	with open('worldcup.teams.csv') as csvfile:
# 		reader=csv.DictReader(csvfile)
# 		for row in reader:
# 			p=WCTeams(AssociationName=row['AssoCode'],Continent=row['Continent'],CountryName=row['Country'],CountryCode=row['Code'])
# 			p.save()


#Mapping for WCup
# path='/home/jubanjan/WCGIS/WC/CSVFiles'
# os.chdir(path)
# a=Stadiums.objects.order_by('stadiumcod')
# def run():
# 	with open('WCup.csv') as csvfile:
# 		reader=csv.DictReader(csvfile)
# 		for row in reader:
# 			for i in a:
# 				if str(i) == row['stadiumcod']:
# 					p = WCup(date=row['date'],MatchName=row['MatchName'],MatchNumber=row['MatchNumber'],stadiumcod=i)
# 					p.save()
# 				else:
# 					print i, row['stadiumcod']


#Mapping for WCStanding
# path='/home/jubanjan/WCGIS/WC/CSVFiles'
# os.chdir(path)
# a=WCTeams.objects.order_by('CountryCode')

# def run():
# 	with open('worldcup.standings.csv') as csvfile:
# 		reader=csv.DictReader(csvfile)
# 		for row in reader:
# 			for i in a:
# 				if str(i) == row['Country']:
# 					# print row['Group'],row['PositionGroup'],row['Points'],row['GoalsAgainst'],row['Played'],row['Won'],row['Drawn'],
# 					p = WCStanding(WCGroupName=row['Group'],CountryCode=i,PositionGroup=row['PositionGroup'],Points=row['Points'],GoalsAgainst=row['GoalsAgainst'],Played=row['Played'],Won=row['Won'],Drawn=row['Drawn'],Loss=row['Losses'])
# 					p.save()
# 				else:
# 					print i, row['Country']

#Mapping for WCMatch
#path='/home/jubanjan/WCGIS/WC/CSVFiles'
#os.chdir(path)
# a=WCup.objects.order_by('MatchNumber')
# def run():
# 	with open('WCMatch.csv') as csvfile:
# 		reader=csv.DictReader(csvfile)
# 		for row in reader:
# 			for i in a:
# 				if str(i) == row['MatchNumber']:
# 					# print row['Group'],row['PositionGroup'],row['Points'],row['GoalsAgainst'],row['Played'],row['Won'],row['Drawn'],
# 					p = WCMatch(MatchNumber=i,MatchLinup=row['MatchLineup'],Score=row['ScoreLine'])
# 					p.save()
# 				else:
# 					print i, row['MatchNumber']


#Mapping for PlayerScores
	

a=WCup.objects.order_by('MatchNumber')

def run():
	with open('PlayerScore.csv') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			for i in a:
				if str(i) == row['MatchNumber']:
					# print row['Group'],row['PositionGroup'],row['Points'],row['GoalsAgainst'],row['Played'],row['Won'],row['Drawn'],
					p = PlayerScore(MatchNumber=i,PlayerName=row['PlayerName'],Minute=row['GoalMinute'],PlayerCountry=row['PlayerCountry'])
					p.save()
				else:
					print i, row['MatchNumber']		
			


