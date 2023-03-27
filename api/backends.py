from django.contrib.auth.backends import BaseBackend
from api.models import User


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
