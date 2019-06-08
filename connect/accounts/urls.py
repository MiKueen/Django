from django.urls import path, reverse_lazy
from . import views
from home.views import HomeView
from django.contrib.auth.views import (
	LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, 
	PasswordResetConfirmView, PasswordResetCompleteView
	)

app_name = 'accounts'

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
	path('signup/', views.signup, name='signup'),
	path('profile/', views.view_profile, name='view_profile'),
	path('profile/<int:pk>/', views.view_profile, name='view_profile_with_pk'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	path('change-password/', views.change_password, name='change_password'),
	path('password-reset/',
         PasswordResetView.as_view(
             template_name='accounts/password_reset_form.html', email_template_name='accounts/password_reset_email.html', subject_template_name='accounts/password_reset_subject.txt',
            success_url=reverse_lazy('accounts:password_reset_done')
         ),
         name='password_reset'),
	path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html', success_url=reverse_lazy('accounts:password_reset_complete')
         ),
         name='password_reset_confirm'),
	path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]