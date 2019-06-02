from django.db import models
from datetime import datetime

class Category(models.Model):
	tut_category = models.CharField(max_length=200)
	cat_summary = models.CharField(max_length=200)
	cat_slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tut_category

class Series(models.Model):
	tut_series = models.CharField(max_length=200)
	tut_category = models.ForeignKey(Category, default=1, verbose_name="Category", on_delete=models.CASCADE)
	ser_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tut_series

class Tutorial(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	published = models.DateTimeField("date published", default=datetime.now())

	tut_series = models.ForeignKey(Series, default=1, verbose_name="Series", on_delete=models.CASCADE)
	tut_slug = models.CharField(max_length=200, default=1)
	
	def __str__(self):
		return self.title

