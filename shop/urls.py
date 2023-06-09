from django.urls import path
from .views import index, single_item, items,tags

app_name = 'shop'

urlpatterns = [
    path('', index),
    path('api/item', single_item),
    path('api/items', items),
    path('api/tags', tags),
]
