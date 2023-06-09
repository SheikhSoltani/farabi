import logging

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shop.models import Item , Tag
from .serializers import ItemSerializer,TagSerializer

logger = logging.getLogger('django')


@api_view(['GET'])
def index(request):
    return Response({
        'as': 'asd'
    })


@api_view(['GET'])
def single_item(request):
    item = get_object_or_404(Item, slug=request.GET.get('slug'))
    aboba = ItemSerializer(item, many=False).data
    logger.info(aboba)
    return Response({
        'item': aboba
    })


@api_view(['GET'])
def items(request):
    return Response({
        'items': ItemSerializer(Item.objects.all(), many=True).data
    })

@api_view(['GET'])
def tags(request):
    return Response({
        'tags': TagSerializer(Tag.objects.all(), many=True).data
    })

