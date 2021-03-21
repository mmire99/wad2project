from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class Register(SuccessMessageMixin,CreateView):
	form_class = SignUpForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('login')
	success_message='%(username)s Welcome to StormWind Herald, Login Here :p'

# @login_required
# def profile(request):
# 	return render(request,'users/profile.html',{})

def updateProfile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
								   request.FILES,
								   instance= request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,instance =request.user.profile)
	context = {
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request,'users/profileUpdate.html',context)