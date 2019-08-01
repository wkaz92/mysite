from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Date', {'fields': ['tutorial_title', 'tutorial_published']}),
        ('Content', {'fields': ['tutorial_content']})
    ]   

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
admin.site.register(Tutorial, TutorialAdmin)
