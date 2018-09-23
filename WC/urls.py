from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='WC'

urlpatterns = [
    url(r'^$',views.WCTeam_render, name="list"),
     url(r'^Stadiums_Data/$',views.Stadiums_Data, name="StadiumsData"),
     url(r'^StadClubs_Data/$',views.StadClub_Data, name="StadClubsData"),
     url(r'^StadClubs_DataJSON/$',views.StadClub_DataSerialize, name="StadClubsDataJSON"),
     url(r'^Chart_Json/$',views.Chart_Json, name="StadChartsDataJSON"),
     url(r'^Routing/$',views.Routing_render, name="Routing"),
      url(r'^Query/$',views.Query_render, name="Query"),
    ]

