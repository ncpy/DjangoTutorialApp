from django.contrib import admin

# Register your models here.
from .models import Tutorial, TutorialSeries, TutorialCategory 
from tinymce.widgets import TinyMCE
from django.db import models

class AdminManagement(admin.ModelAdmin):
	#fields = ['tutorial_title',
	#		  'tutorial_published',
	#		  'tutorial_content']

	fieldsets = [
		("Title/date", {'fields':['tutorial_title','tutorial_published']}),
		("URL", {'fields':["tutorial_slug"]}),
		("Series", {'fields':["tutorial_series"]}),
		("Content", {'fields':["tutorial_content"]})
	]

	formfield_overrides = {
		models.TextField: {'widget':TinyMCE()}
	}

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)

admin.site.register(Tutorial, AdminManagement)

