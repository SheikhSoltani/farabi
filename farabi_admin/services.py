from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import get_object_or_404

User = get_user_model()


def authenticate_user(request, log_data):
    """ Authenticate user """
    user = authenticate(request, username=log_data['username'], password=log_data['password'])
    if user:
        login(request, user)
        return True
    return False
