from django import forms

from .models import *

from django.forms import ModelChoiceField


class NamesChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return '{StadiumName}'.format(StadiumName=obj.stadiumnam)



class RawQueryForm(forms.Form):

	StadiumName= NamesChoiceField(queryset = Stadiums.objects.filter(worldcup='WorldCup2014'),initial=0)
	#StadiumName= forms.ModelChoiceField(queryset = Stadiums.objects.all(),initial=0)