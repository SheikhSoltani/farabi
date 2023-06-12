from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import get_object_or_404

User = get_user_model()


def authenticate_user(request, log_data) -> bool:
    """ Authenticate user """
    user = authenticate(request, username=log_data['username'], password=log_data['password'])
    if user:
        login(request, user)
        return True
    return False


def logged_or_not(request) -> bool:
    """ Check if user is logged in """
    if request.user.is_authenticated:
        return True
    return False
