from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username','email','password1','password2')

	def __init__(self,*args,**kwargs):
		super(SignUpForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(
		required = False,
		widget=forms.EmailInput(attrs={'class':'form-control'}))
	username = forms.CharField(
		required = True,
		widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ('username','email')

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_pic']