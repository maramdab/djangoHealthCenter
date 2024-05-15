from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName=models.CharField(max_length=100)
    secondName=models.CharField(max_length=100)
    dateOfBirth=models.DateField(default=timezone.now)
    genderChoices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=genderChoices, default='O')
 



    def __str__(self):
        return f"{self.firstName} ,{self.secondName}"

class Services(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='static/media/')
    icon=models.CharField(max_length=100,default='fa-solid fa-hospital-user')
    

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})

    def __str__(self):
        return f'{self.name}'

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    medical_number=models.IntegerField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='static/media/')


    def __str__(self):
        return f'Doctor : {self.name}, MN: {self.medical_number},Service : {self.service}'

class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    service=models.ForeignKey(Services,on_delete=models.CASCADE)
    contact_num = models.CharField(validators=[phone_validator], max_length=17, blank=True)

    def get_absolute_url(self):
        return reverse('patient',kwargs={'pk':self.pk})

    def __str__(self):
        return f'Appointment for: {self.patient}, On: {self.appointment_date}'


