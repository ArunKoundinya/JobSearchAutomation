from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success_page'),
    path('job-search-results/', views.job_search_results, name='job_search_results'),
    path('download_csv/<int:job_search_id>/', views.download_csv, name='download_csv'),
]
