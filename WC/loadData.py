import os
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
from .models import StadClub

#Load Mapping Dictionary Here

stadclub_mapping = {
    'team' : 'Team',
    'fdcouk' : 'FDCOUK',
    'city' : 'City',
    'stadium' : 'Stadium',
    'capacity' : 'Capacity',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'country' : 'Country',
    'geom' : 'MULTIPOINT',
}


#Command for generating model template -->   python manage.py ogrinspect SHPFiles/WC/Output.shp  Stadiums --srid=4326 --mapping --multi

SourceFile=os.path.abspath(os.path.join(os.path.dirname(__file__),'SHPFiles/WC_Clubs/StadiumExtra.shp'))


def run(verbose=True):
	lm=LayerMapping(StadClub,SourceFile,stadclub_mapping,transform=False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)


