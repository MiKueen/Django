from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	description = models.CharField(max_length=100,default='')
	city =models.CharField(max_length=100, default='')
	phone = models.IntegerField(default=0)
	image = models.ImageField(upload_to='user_profile_images', blank=True)

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
