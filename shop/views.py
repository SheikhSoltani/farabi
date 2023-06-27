import logging
import random

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from shop.models import Item , Tag
from .cart import Cart
from .serializers import ItemSerializer,TagSerializer
from .services import send_mail_to_address

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
    return Response({
        'item': aboba
    })


@api_view(['GET'])
def items(request):
    return Response({
        'items': ItemSerializer(Item.objects.all(), many=True).data
    })


@api_view(['GET'])
def main_page_items(request):
    items_query = list(Item.objects.all())
    random_items = random.sample(items_query, 4)

    return Response({
        'items': ItemSerializer(random_items, many=True).data
    })


@api_view(['GET'])
def tags(request):
    return Response({
        'tags': TagSerializer(Tag.objects.all(), many=True).data
    })


@csrf_protect
@csrf_exempt
@api_view(['POST'])
def add_to_cart(request):
    cart = Cart(request)
    item = get_object_or_404(Item, id=request.data['item_id'])
    cart.add(item)
    return Response({
        'result': True
    })


@api_view(['POST'])
def delete_from_cart(request):
    cart = Cart(request)
    cart.remove(get_object_or_404(Item, id=request.data['item_id']))
    return Response({
        'result': True
    })


@api_view(['POST'])
@csrf_exempt
def flush_cart(request):
    cart = Cart(request)
    cart.clear()
    return Response({'result': True})


@api_view(['GET'])
def get_cart_items(request):
    cart = Cart(request)
    return Response({
        'items': cart
    })


@api_view(['GET'])
def get_items_count_in_cart(request):
    cart = Cart(request)
    return Response({
        'length': cart.len()
    })


@api_view(['POST'])
def send_mail(request):
    send_mail_to_address(request.data['name'], request.data['phone'], request.data['email'])