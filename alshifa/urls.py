from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('aboutUs/',about,name='about')

]