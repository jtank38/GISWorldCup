from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from .forms import RawQueryForm
from collections import Counter





def WCTeam_render(request):
	
	Teams=WCTeams.objects.all().values()
	
	return render(request,'WC/leaflet_render.html',{'WCTeams':Teams})


def Stadiums_Data(request):
	
	StadiumsData=serialize('geojson',Stadiums.objects.all())
	
	return HttpResponse(StadiumsData,content_type='json')

def StadClub_Data(request):
	
	StadClubData=serialize('geojson',StadClub.objects.all())
	
	return HttpResponse(StadClubData,content_type='json')


def StadClub_DataSerialize(request):
	StadClubJSONData=serialize("json", StadClub.objects.all())

	return HttpResponse(StadClubJSONData,content_type='json')


def Routing_render(request):

	ClubStadium=StadClub.objects.all().values()
	
	return render(request,'WC/Try_Cluster.html',{'StadClubs':ClubStadium})



def Query_render(request):
	stadiumform=RawQueryForm()

	#stadiumform.fields['StadiumName'].queryset = Stadiums.objects.filter(worldcup='WorldCup2014')
	#StadiumData=Stadiums.objects.filter(worldcup='WorldCup2014')
	print request.POST
	context={
		"form":stadiumform
	}
	# StadiumData=Stadiums.objects.filter(worldcup='WorldCup2014')
	return render(request,'WC/Query.html',context)


def Chart_Json(request):
	start='WC-2018'
	Labels1=StadClub.objects.values_list('stadium', flat=True)
	val1=StadClub.objects.values_list('capacity', flat=True)
	val_convert=map(int,val1)
	dicta={}
	for ind,vals in enumerate(Labels1):
		dicta[vals]=val_convert[ind]

	Labels2=StadClub.objects.values_list('country', flat=True)
	dictc=Counter(Labels2)
	

	Labels3_wc2018=PlayerScore.objects.filter(MatchNumber__MatchNumber__contains=start).values_list('PlayerCountry', flat=True)
	Labels3_wc2014=PlayerScore.objects.filter(~Q(MatchNumber__MatchNumber__contains=start)).values_list('PlayerCountry', flat=True)
	
	dictd_1=Counter(Labels3_wc2014)
	dictd_2=Counter(Labels3_wc2018)
	dictd={"Dataset2014":dictd_1,"Dataset2018":dictd_2}
	
	Labels4_wc2018=WCTeams.objects.filter(CountryCode__startswith=start).values_list('Continent', flat=True)
	Labels4_wc2014=WCTeams.objects.filter(~Q(CountryCode__startswith=start)).values_list('Continent', flat=True)
	
	dictb_1=Counter(Labels4_wc2014)
	dictb_2=Counter(Labels4_wc2018)
	dictb={"Dataset2014":dictb_1,"Dataset2018":dictb_2}
	
	
	FinalDict={'Chart1':dicta,'Chart2':dictb,'Chart3':dictc,'Chart4':dictd}

	return JsonResponse(FinalDict)