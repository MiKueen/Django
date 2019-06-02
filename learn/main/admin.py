from django.contrib import admin
from .models import Tutorial, Series, Category
from tinymce.widgets import TinyMCE
from django.db import models

class Admin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["title", "published"]}),
		("URL", {"fields":["tut_slug"]}),
		("Series", {"fields":["tut_series"]}),
		("Content", {"fields":["content"]})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(Series)
admin.site.register(Category)
admin.site.register(Tutorial, Admin)