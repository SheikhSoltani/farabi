from django.contrib.auth import login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Tag, Item
from shop.serializers import ItemSerializer
from .services import authenticate_user, logged_or_not

import logging
logger = logging.getLogger('django')


@csrf_exempt
@api_view(['POST'])
def log_in(request):
    """ Process of login in  """
    logger.info(request.data)
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

@csrf_exempt
@api_view(['POST'])
def log_out(request):
    logout(request)
    return Response({
        'result': True
    })


@csrf_exempt
@api_view(['POST'])
def add_tag(request):
    Tag.create_tag(request.data)
    return Response({
        'result': True
    })


@csrf_exempt
@api_view(['POST'])
def delete_tag(request):
    Tag.delete_tag(request.data)
    return Response({
        'result': True
    })


@csrf_exempt
@api_view(['PATCH'])
def edit_tag(request):
    Tag.edit_tag(request.data)
    return Response({
        'result': True
    })


@csrf_exempt
@api_view(['POST'])
def add_item(request):
    try:
        Item.create_item(request.data)
    except Exception as e:
        return Response({
            'result': False
        })
    return Response({
        'result': True
    })




@csrf_exempt
@api_view(['PATCH'])
def edit_item(request):
    Item.edit_item(request.data)
    return Response({
        'result': True
    })


@csrf_exempt
@api_view(['POST'])
def delete_item(request):
    Item.delete_item(request.data)
    return Response({
        'result': True
    })


@csrf_exempt
@api_view(['GET'])
def logged(request: WSGIRequest):
    result = logged_or_not(request)
    if result:
        return Response({'result': True})
    else:
        return Response({'result': False})