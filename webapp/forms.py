from django import forms
from .models import CustomerDetail, Appointment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetail
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'email']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time', 'appointment_type', 'additional_notes']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'

        
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']