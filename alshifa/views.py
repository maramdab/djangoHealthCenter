from django.shortcuts import render,redirect,get_object_or_404
from .form import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    service = Services.objects.all()
    doctor=Doctor.objects.all()
    context={'service':service,'doctor':doctor}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

@login_required(login_url='/accounts/login/')
def appointment(request):
    
    services=Services.objects.all()
    if request.method == 'POST':
        contact_num = request.POST['phoneNumber']
        appointment_date_str=request.POST['date']
        appointment_time_str=request.POST['time']
        selected_service=request.POST['servicesOption']
        email=request.POST['email']
        first_name = request.POST['firstName']
        second_name = request.POST['secondName']
        birthday_str = request.POST['birthday']
        service_name=Services.objects.get(name=selected_service)
        doctor=Doctor.objects.filter(service=service_name).first()
        gender=request.POST['gender']

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")
            return render(request, 'appointment.html', {'services': services})  

        try:
            birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid date of birth format.")
            return render(request, 'appointment.html', {'services': services})
        try:
            appointment_date = datetime.strptime(appointment_date_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid appointment date format.")
            return render(request, 'appointment.html', {'services': services})

        # Parse and validate the appointment time
        try:
            appointment_time = datetime.strptime(appointment_time_str, '%H:%M').time()
        except ValueError:
            messages.error(request, "Invalid appointment time format.")
            return render(request, 'appointment.html', {'services': services})

        try:
            patient=Patient.objects.get(user=user)
        except Patient.DoesNotExist:   
            patient = Patient.objects.create(
                user=user,
                firstName=first_name,
                secondName=second_name,
                dateOfBirth=birthday,
                gender=gender
            )
        existing_appointments_count = Appointment.objects.filter(
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).count()

        if existing_appointments_count >= 2:
            messages.error(request, "There are already two appointments at this date and time. Please choose a different time.")
            return render(request, 'appointment.html', {'services': services})



        appointment = Appointment.objects.create(
        patient=patient,
        appointment_date=appointment_date,
        appointment_time=appointment_time,
        doctor=doctor,
        service=service_name,
        contact_num=contact_num
            )
        return redirect('/patientInfo/')
        

    return render(request, 'appointment.html', {'services': services})

def contact(request):
    return render(request,'contact.html')


def patientInfo(request,pk):
    appointment=Appointment.objects.get(pk=pk)
    patient_info=Patient.objects.get(name=appointment)
    context={'patient_info':patient_info,
              'appointment':appointment
             }

    return render(request,'patientInfo.html',context)

def services(request):
    service = Services.objects.all()
    context={'service':service}
    return render(request,'servicesNew.html',context)

def logout(request):
    request.session.flush()
    return redirect('/accounts/login')

def signUp(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request,'register.html',{'form':form}) 
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid ():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('/')
        else:
            return render(request,'register.html',{'form':form}) 

def services_details(request,pk):
    service= get_object_or_404(Services,pk=pk)

    return render(request,'service_detail.html',{'service':service})

