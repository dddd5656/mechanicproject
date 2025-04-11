from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm, ContactForm, ServiceRequestForm
import json
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def appointment(request):
    form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def testimonials(request):
    return render(request, 'testimonials.html')

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

@csrf_exempt
def book_appointment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Create new appointment
            appointment = Appointment.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                service=data.get('service'),
                date=datetime.strptime(data.get('date'), '%Y-%m-%d').date(),
                message=data.get('message', '')
            )
            
            return JsonResponse({
                'status': 'success',
                'message': 'Appointment booked successfully!'
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid data format'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=405)

def submit_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            try:
                appointment = form.save()
                messages.success(request, 'Your appointment has been booked successfully!')
                return render(request, 'appointment.html', {
                    'appointment_success': True,
                    'appointment_id': appointment.id
                })
            except Exception as e:
                messages.error(request, f'Error saving appointment: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Process the form data (e.g., send email)
                contact = form.save()
                messages.success(request, 'Your message has been sent successfully!')
                return render(request, 'contact.html', {
                    'contact_success': True
                })
            except Exception as e:
                messages.error(request, f'Error sending message: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            # Process the form data
            messages.success(request, 'Your service request has been submitted successfully!')
            return redirect('services')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ServiceRequestForm()
    return render(request, 'services.html', {'form': form})
