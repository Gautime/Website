from django.contrib.auth.models import User
from django import forms


class UserForms(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
   #/class meta is basically the information about your class/
	class Meta: 
	 	model = User

	 	fields=['username', 'email', 'password']