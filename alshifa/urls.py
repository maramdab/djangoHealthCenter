from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('aboutUs/',about,name='about'),
    path('appointment/',appointment,name='appointment'),
    path('contactUs/',contact,name='contact'),
    path('register/',signUp,name='register'),
    path('patientInfo/',patientInfo,name='patient'),
    path('services/',services,name='services'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('services/<int:pk>/',services_details,name='details'),
   path('page-delete/', delete_object_function, name='delete_object'),
   path('doctor/sign_in/', doctor_sign_in, name='doctor_sign_in'),
   path('doctor_dashboard/',doctor_dashboard,name='doctor_dashboard'),
   path('doctor/appointments/',appointment_list,name='appointment_list'),
   path('doctor/patient_list/',patients_list,name='patients_list'),



]
