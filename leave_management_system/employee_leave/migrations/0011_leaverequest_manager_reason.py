# Generated by Django 5.1.3 on 2024-11-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_leave', '0010_leaverequest_hr'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='manager_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
