from django.shortcuts import render, redirect, HttpResponse
from accounts.forms import SignUpForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

def home(request):
	return render(request, 'accounts/home.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts')
	else:
		form = SignUpForm()
		args = {'form': form}
		return render(request, 'accounts/signup.html', args)

def view_profile(request):
	args = {'user': request.user}
	return render(request, 'accounts/profile.html')

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/accounts/profile')

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts/edit_profile.html', args)