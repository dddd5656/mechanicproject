from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('api/book-appointment/', views.book_appointment, name='book_appointment'),
    path('submit-appointment/', views.submit_appointment, name='submit_appointment'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path('service-request/', views.service_request, name='service_request'),
] 