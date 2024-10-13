from django.shortcuts import render, redirect
from django.http import HttpResponse  # Import HttpResponse
from .forms import AcceptInputForm
from .models import JobSearch
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Scraping.Indeed import scrape_indeed



def home(request):
    if request.method == 'POST':
        form = AcceptInputForm(request.POST)
        if form.is_valid():
            # Get the form data
            platform = form.cleaned_data['platform']
            jobsearch = form.cleaned_data['jobsearch']  # e.g., "data+science+manager"
            location = form.cleaned_data['location']    # e.g., "United+States"
            pages = form.cleaned_data['pages']          # e.g., number of pages (as a string)
            
            results_directory = 'results'
            if not os.path.exists(results_directory):
                os.makedirs(results_directory)

            # Check if the platform is Indeed, then trigger the scraper
            if platform == 'Indeed':
                # Convert jobsearch, location, and pages to the format expected by your scraper
                jobsearch_query = jobsearch.replace(" ", "+")
                location_query = location.replace(" ", "+")
                page_number = int(pages)  # Assuming this is already the correct value

                # Call the main_scrape function with these parameters
                scraped_data = scrape_indeed(jobsearch_query, location_query, "1", page_number)  # Example: scraping 5 results per page
                
                # Save the scraped data to a CSV file
                csv_file_path = f"{results_directory}/{jobsearch}_results_{location}_data.csv"
                scraped_data.to_csv(csv_file_path, index=False)
                
                # Create a JobSearch instance using the correct field names
                job_search = JobSearch(
                    platform=platform,
                    jobsearch=jobsearch,  # Corrected to match model field
                    location=location,
                    pages=pages,  # Changed from page_number to pages
                    csv_file=csv_file_path  # Ensure this is the correct path
                )
                job_search.save()
                
                # Optional: You can redirect to the success page and also pass a message about the CSV file
                return render(request, 'JobSearchAuto/success.html', {'file_name': f"{jobsearch}_results_{location}_data.csv"})

    else:
        form = AcceptInputForm()

    return render(request, 'JobSearchAuto/home.html', {'form': form})


def success(request):
    return render(request, 'JobSearchAuto/success.html')


def job_search_results(request):
    job_searches = JobSearch.objects.all()  # Fetch all stored job search data
    return render(request, 'JobSearchAuto/job_search_results.html', {'job_searches': job_searches})


def download_csv(request, job_search_id):
    # Get the job search object
    job_search = JobSearch.objects.get(id=job_search_id)

    # Create an HTTP response with the CSV content
    response = HttpResponse(
        content_type='text/csv',
        headers={
            'Content-Disposition': f'attachment; filename="{job_search.csv_file.name}"',
        },
    )

    # Read the CSV file and write it to the response
    with open(job_search.csv_file.path, 'rb') as csvfile:
        response.write(csvfile.read())

    return response
