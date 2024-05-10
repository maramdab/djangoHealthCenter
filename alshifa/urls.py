from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('aboutUs/',about,name='about'),
    path('appointment/',appointment,name='appointment'),
    path('contactUs/',contact,name='contact'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('patientInfo',patientInfo,name='patient'),
    path('services/',services,name='services'),

]