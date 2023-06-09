from django.contrib import admin
from django.urls import path, include
from .views import log_in, log_out, add_item

app_name = 'farabi_admin'

urlpatterns = [
    path('login', log_in),
    path('logout', log_out),
    path('create-item', add_item)
]
