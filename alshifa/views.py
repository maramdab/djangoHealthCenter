from django.shortcuts import render,redirect,get_object_or_404
from .form import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *

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
    return render(request,'appointment.html')

def contact(request):
    return render(request,'contact.html')


def patientInfo(request):
    return render(request,'patientInfo.html')

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

