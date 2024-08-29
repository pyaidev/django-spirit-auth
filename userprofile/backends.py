# backends.py
from django.contrib.auth.backends import ModelBackend
from .models import SiteUser

class SiteUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = SiteUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except SiteUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return SiteUser.objects.get(pk=user_id)
        except SiteUser.DoesNotExist:
            return None
