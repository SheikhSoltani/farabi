from django.urls import path
from .views import index, single_item, items, tags, add_to_cart, delete_from_cart, flush_cart, get_cart_items, get_items_count_in_cart, main_page_items

app_name = 'shop'

urlpatterns = [
    path('', index),
    path('api/item', single_item),
    path('api/items', items),
    path('api/tags', tags),
    path('api/add-to-cart', add_to_cart),
    path('api/get-cart-items', get_cart_items),
    path('api/delete-from-cart', delete_from_cart),
    path('api/flush-cart', flush_cart),
    path('api/main_page_items', main_page_items),
    path('api/get_length_cart', get_items_count_in_cart),
]
