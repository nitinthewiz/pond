from django import forms
from pond.models import Reflection
from django.contrib.auth.models import User

class ReflectionForm(forms.ModelForm):
	class Meta:
		model = Reflection
		fields = ()

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password')