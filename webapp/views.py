from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import AppointmentForm, RegistrationForm, CustomerDetailsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .models import Appointment, CustomerDetail, ServiceType
from django.contrib import messages

def home_view(request):
    appointments = Appointment.objects.all()
    service_types = ServiceType.objects.all()

    return render(request, 'pages/home.html', {'appointments': appointments, 'service_types': service_types})
 

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('customer_details_form')
    else:
        form = RegistrationForm()
    
    return render(request, 'pages/registration_form.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'pages/login.html', {'form': form})

def custom_logout(request):
    if request.method == 'POST':
        
        django_logout(request)
        return redirect('home')
    else:
       
        return render(request, 'pages/confirmation_logout.html')

# APPOINTMENT INFO
@login_required
def appointment_form_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('home')
    else:
        form = AppointmentForm()

    return render(request, 'pages/appointment_form.html', {'form': form})

@login_required
def view_appointments(request):
    user_appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'pages/view_appointments.html', {'user_appointments': user_appointments})

@login_required
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id, user=request.user)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('view_appointments')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'pages/update_appointment.html', {'form': form})

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id, user=request.user)

    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment canceled successfully.')
        return redirect('view_appointments')

    return redirect('view_appointments')

@login_required
def customer_details_view(request):
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            customer_details = form.save(commit=False)
            customer_details.user = request.user
            customer_details.save()
            return redirect('appointment_form')
    else:
        form = CustomerDetailsForm()
    
    return render(request, 'pages/customer_details.html', {'form': form})

@login_required
def view_CustomerDetails(request):
    user_CustomerDetails = CustomerDetail.objects.filter(user=request.user)
    return render(request, 'pages/view_customerDetails.html', {'user_CustomerDetails': user_CustomerDetails})





