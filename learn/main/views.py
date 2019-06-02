from django.shortcuts import render, redirect
from .models import Tutorial, Category, Series
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login

def single_slug(request, single_slug):
    categories = [c.cat_slug for c in Category.objects.all()]
    if single_slug in categories:
        matching_series = Series.objects.filter(tut_category__cat_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tut_series__tut_series=m.tut_series).earliest("published")
            series_urls[m] = part_one.tut_slug

        return render(request=request,
                      template_name='main/category.html',
                      context={"tut_series": matching_series, "part_ones": series_urls})

    tutorials = [t.tut_slug for t in Tutorial.objects.all()]

    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tut_slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(tut_series__tut_series=this_tutorial.tut_series).order_by('published')
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)

        return render(request=request,
                      template_name='main/tutorial.html',
                      context={"tutorial": this_tutorial,
                               "sidebar": tutorials_from_series,
                               "this_tut_idx": this_tutorial_idx})

def home(request):
    return render(request = request,
                  template_name='main/categories.html',
                  context = {"categories": Category.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:home")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def logout_user(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:home")
