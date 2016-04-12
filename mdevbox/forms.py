from mdevbox.models import *
from django.contrib.auth.models import User
from django import forms
from .models import *






#-------------------------------------------------------------------------------------------------------------------- user auth
class authentication(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username',  'password', 'email',  'first_name','last_name')
