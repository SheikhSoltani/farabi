from django.contrib.auth import login, logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import authenticate_user

import logging
logger = logging.getLogger('django')


@api_view(['POST'])
@csrf_exempt
def log_in(request):
    """ Process of login in  """
    logger.debug(request.data)
    if request.user.is_authenticated:
        return Response({
            'already logged': True
        })

    result = authenticate_user(request, request.data)

    if result:
        return Response({
            'logged': result
        })
    else:
        return Response({
            'logged': 'False, failed'
        })


@api_view(['POST'])
@csrf_exempt
def log_out(request):
    logout(request)
    return Response({
        'result': True
    })
