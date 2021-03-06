from django.views.generic import TemplateView
from .forms import HomeForm
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all().order_by('create_time')
		users = User.objects.all()

		args = {'form': form, 'posts': posts, 'users': users}
		return render(request, self.template_name, args)

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']
			form = HomeForm()
			return redirect('home:home')

		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)
