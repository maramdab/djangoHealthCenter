from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Doctor

class MedicalNumberBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            doctor = Doctor.objects.get(medical_number=username)
            user = doctor.user
            if user.check_password(password):
                return user
        except Doctor.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
