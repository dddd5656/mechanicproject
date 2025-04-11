from django import forms
from .models import Appointment, Contact, ServiceRequest, Service, Testimonial, TeamMember, FAQ

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'service', 'date', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Basic validation for phone number
        if not phone.isdigit() and not all(c in '+-() ' for c in phone if not c.isdigit()):
            raise forms.ValidationError("Please enter a valid phone number")
        return phone
        
    def clean_date(self):
        date = self.cleaned_data.get('date')
        from datetime import date as today_date
        if date < today_date.today():
            raise forms.ValidationError("Appointment date cannot be in the past")
        return date

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your Message'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required")
        return email

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = [
            'name', 'email', 'phone', 'vehicle_type', 
            'vehicle_make', 'vehicle_model', 'vehicle_year',
            'service_description', 'preferred_date'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'vehicle_make': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_model': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'service_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'preferred_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Basic validation for phone number
        if not phone.isdigit() and not all(c in '+-() ' for c in phone if not c.isdigit()):
            raise forms.ValidationError("Please enter a valid phone number")
        return phone
        
    def clean_preferred_date(self):
        date = self.cleaned_data.get('preferred_date')
        from datetime import date as today_date
        if date < today_date.today():
            raise forms.ValidationError("Preferred date cannot be in the past")
        return date

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'rating', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required")
        return email 