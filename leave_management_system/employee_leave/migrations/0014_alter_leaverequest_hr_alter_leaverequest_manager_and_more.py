# Generated by Django 5.1.3 on 2024-11-28 15:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_leave', '0013_leaverequest_hr_reason'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='hr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_manager_hr_leave_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_manager_leave_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('manager_approved', 'Manager Approved'), ('manager_rejected', 'Manager Rejected'), ('hr_approved', 'HR Approved'), ('hr_rejected', 'HR Rejected')], default='pending', max_length=20),
        ),
    ]
