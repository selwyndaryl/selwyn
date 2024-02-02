from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('appointment-form/', views.appointment_form_view, name='appointment_form'),
    path('view-appointments/', views.view_appointments, name='view_appointments'),
    path('update-appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('cancel-appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('customer-details/', views.customer_details_view, name='customer_details_form'),
    path('view-customer-details/', views.view_CustomerDetails, name='view_customer_details'),
]




