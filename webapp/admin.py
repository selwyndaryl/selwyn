from django.contrib import admin
from .models import CustomerDetail, Appointment, AppointmentStatus, ServiceType

@admin.register(CustomerDetail)
class CustomerDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'address', 'phone_number', 'email')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'appointment_date', 'appointment_time', 'appointment_type', 'get_status')

    def get_status(self, obj):
        return obj.status.status if obj.status else None
    get_status.short_description = 'Status'

@admin.register(AppointmentStatus)
class AppointmentStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)





