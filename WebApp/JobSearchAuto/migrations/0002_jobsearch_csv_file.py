# Generated by Django 5.1.2 on 2024-10-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("JobSearchAuto", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobsearch",
            name="csv_file",
            field=models.FileField(blank=True, null=True, upload_to="results/"),
        ),
    ]
