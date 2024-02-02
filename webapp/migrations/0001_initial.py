# Generated by Django 5.0 on 2024-01-23 06:29

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(default=datetime.date.today)),
                ('appointment_time', models.TimeField(default=None)),
                ('appointment_type', models.CharField(max_length=50)),
                ('additional_notes', models.TextField(default='No additional notes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('services', models.ManyToManyField(to='webapp.appointmentservice')),
                ('status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.appointmentstatus')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
