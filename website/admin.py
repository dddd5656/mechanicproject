from django.contrib import admin
from .models import (
    Appointment, Contact, ServiceRequest, 
    Service, Testimonial, TeamMember, FAQ
)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'date', 'status', 'created_at')
    list_filter = ('service', 'status', 'date')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at',)
    ordering = ('-date', '-created_at')
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Appointment Details', {
            'fields': ('service', 'date', 'message')
        }),
        ('Status Information', {
            'fields': ('status', 'created_at')
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message Details', {
            'fields': ('subject', 'message')
        }),
        ('Status Information', {
            'fields': ('is_read', 'created_at')
        }),
    )

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'vehicle_type', 'vehicle_make', 'vehicle_model', 'status', 'created_at')
    list_filter = ('vehicle_type', 'status', 'created_at')
    search_fields = ('name', 'email', 'phone', 'vehicle_make', 'vehicle_model')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Vehicle Information', {
            'fields': ('vehicle_type', 'vehicle_make', 'vehicle_model', 'vehicle_year')
        }),
        ('Service Details', {
            'fields': ('service_description', 'preferred_date')
        }),
        ('Status Information', {
            'fields': ('status', 'created_at')
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
    ordering = ('name',)
    
    fieldsets = (
        ('Service Information', {
            'fields': ('name', 'description', 'price')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Status Information', {
            'fields': ('is_featured', 'created_at')
        }),
    )

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved', 'created_at')
    search_fields = ('name', 'email', 'comment')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email')
        }),
        ('Testimonial Details', {
            'fields': ('rating', 'comment')
        }),
        ('Status Information', {
            'fields': ('is_approved', 'created_at')
        }),
    )

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'phone', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'position', 'email', 'phone', 'bio')
    readonly_fields = ('created_at',)
    ordering = ('name',)
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'position', 'bio')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Status Information', {
            'fields': ('is_active', 'created_at')
        }),
    )

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('question', 'answer')
    readonly_fields = ('created_at',)
    ordering = ('question',)
    
    fieldsets = (
        ('FAQ Information', {
            'fields': ('question', 'answer')
        }),
        ('Status Information', {
            'fields': ('is_active', 'created_at')
        }),
    )
