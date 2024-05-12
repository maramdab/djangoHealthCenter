from django.db import models
from django.utils import timezone

# Create your models here.

class Patient(models.Model):
    firstName=models.CharField(max_length=100)
    secondName=models.CharField(max_length=100)
    dateOfBirth=models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.firstName} ,{self.secondName}"

class Services(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='static/media/')

    def __str__(self):
        return f'{self.name}'

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    medical_number=models.IntegerField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        return f'Doctor : {self.name}, MN: {self.medical_number},Service : {self.service}'

class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointment_date=models.DateTimeField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    service=models.ForeignKey(Services,on_delete=models.CASCADE)

    def __str__(self):
        return f'Appointment for: {self.patient}, On: {self.appointment_date}'


