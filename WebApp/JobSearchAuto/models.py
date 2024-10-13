from django.db import models

# Create your models here.
class JobSearch(models.Model):
    PLATFORM_CHOICES = [
        ('Indeed', 'Indeed'),
        ('GlassDoor', 'GlassDoor'),
        ('Naukri', 'Naukri')
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    jobsearch = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    pages = models.CharField(max_length=10, blank=True, null=True)
    csv_file = models.FileField(upload_to='results/', blank=True, null=True)  # Removed unsupported parameters

    def __str__(self):
        return f"{self.platform} - {self.jobsearch} ({self.location})"
