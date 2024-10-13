from django.contrib import admin
from .models import JobSearch

# Register your models here.
@admin.register(JobSearch)
class JobSearchAdmin(admin.ModelAdmin):
    list_display = ('platform', 'jobsearch', 'location', 'pages')