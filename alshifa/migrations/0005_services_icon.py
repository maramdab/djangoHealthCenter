# Generated by Django 4.2.13 on 2024-05-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alshifa', '0004_alter_doctor_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='icon',
            field=models.CharField(default='fa-solid fa-hospital-user', max_length=100),
        ),
    ]
