from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def appointment(request):
    return render(request,'appointment.html')

def contact(request):
    return render(request,'contact.html')


def register(request):
    return render(request,'register.html')

def patientInfo(request):
    return render(request,'patientInfo.html')

def services(request):
    return render(request,'services.html')

def logout(request):
    request.session.flush()
    return redirect('/accounts/login')