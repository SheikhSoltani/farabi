from django.contrib.auth import get_user_model, authenticate, login
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404

import logging
logger = logging.getLogger('django')

User = get_user_model()


def authenticate_user(request: WSGIRequest, log_data) -> bool:
    """ Authenticate user """
    user = authenticate(request, username=log_data['username'], password=log_data['password'])
    if user:
        login(request, user)
        return True
    return False


def logged_or_not(request: WSGIRequest):
    """ Check if user is logged in """
    if request.user.is_authenticated:
        return True
    return False
