from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	create_time = models.DateTimeField(auto_now_add=True,null=True)
	update_time = models.DateTimeField(auto_now=True)

