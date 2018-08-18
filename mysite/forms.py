from django import forms

from mysite.models import *

class FeedbackForm(forms.ModelForm):
	pass;

class CompareForm(forms.ModelForm):
	player1 = forms.CharField(max_length=120,required=False)
	player2 = forms.CharField(max_length=120,required=False)
	player3 = forms.CharField(max_length=120,required=False)
	player4 = forms.CharField(max_length=120,required=False)

	class Meta:
		model = Player
		fields = ('name',)

