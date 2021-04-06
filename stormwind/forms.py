from django import forms
from .models import Thread,Category,Reply

class ThreadForm(forms.ModelForm):
	class Meta:
		model = Thread
		fields = ('title','category','content')

		widgets = {
			'title' : forms.TextInput(attrs={'class':'form-control'}),
			'category' : forms.Select(choices = 
				[x for x in Category.objects.all().values_list('name','name')]
				,attrs={'class':'form-control'})
		}

class ReplyForm(forms.ModelForm):
	
	class Meta:
		model = Reply
		fields = ('body',)

		widgets = {
			'body' : forms.Textarea(attrs={'class':'form-control'}),		
		}
