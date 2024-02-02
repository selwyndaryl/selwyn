from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class AppointmentStatus(models.Model):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELLED, 'Cancelled'),
    ]

    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return self.status

class ServiceType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CustomerDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Details"

class Appointment(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.TimeField(default=timezone.now)
    appointment_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    additional_notes = models.TextField(default='No additional notes')
    status = models.ForeignKey(AppointmentStatus, on_delete=models.SET_NULL,default=1, null=True) 

    def __str__(self):
        return f"Appointment for {self.user.username}"
