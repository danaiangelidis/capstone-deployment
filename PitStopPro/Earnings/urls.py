from django.urls import path
from . import views

urlpatterns = [
    # Path for viewing earnings by period
    path('view/<str:period>/', views.earnings_view, name='earnings_view'),
    
    # Path for downloading the report
    path('download/<str:period>/', views.download_report, name='download_report'),

    path('update-graph/', views.update_graph, name='update_graph'),
]