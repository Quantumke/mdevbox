from mdevbox.models import *
from django.contrib.auth.models import User
from django import forms
from .models import *






#-------------------------------------------------------------------------------------------------------------------- user auth
class developersemployment(forms.ModelForm):

	class Meta:
		model = developers_employment
		fields = ('email',  'speciality', 'previous_employer',  'role_previous_employment','begin_previous_employment','end_previous_employment')

class developerseducation(forms.ModelForm):
	class Meta:
		model=developers_education
		fields=('highest_education', 'institute_name','begin_education','end_education')

class developersportfolio(forms.ModelForm):
	class Meta:
		model=developers_portfolio
		fields=( 'portfoli_name', 'portfoli_tech', 'portfoli_link', 'portfoli_desc',)
