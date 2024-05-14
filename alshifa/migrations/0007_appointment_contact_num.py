# Generated by Django 4.2.13 on 2024-05-13 23:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alshifa', '0006_doctor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='contact_num',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]