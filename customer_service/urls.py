from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.dashboard, name='dashboard'),
    path('home/', views.dashboard, name='home'),  # Add this as a fallback
    
    # Service request URLs
    path('service-requests/create/', views.create_service_request, name='create_service_request'),
    path('service-requests/<int:pk>/', views.service_request_detail, name='service_request_detail'),
    path('service-requests/<int:pk>/update-status/', views.update_service_request_status, name='update_service_request_status'),
    path('service-requests/<int:pk>/cancel/', views.cancel_service_request, name='cancel_service_request'),
    path('service-requests/', views.my_service_requests, name='my_service_requests'),
]