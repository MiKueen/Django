from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path("", views.home, name="home"),
	path("register/", views.register, name="register"),
	path("login", views.login_user, name="login"),
	path("logout", views.logout_user, name="logout"),
	path("<single_slug>", views.single_slug, name="single_slug"),
]