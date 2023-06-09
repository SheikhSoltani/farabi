from django.contrib import admin
from django.urls import path, include
from .views import log_in, log_out, add_item, edit_item, delete_item, add_tag, edit_tag, delete_tag

app_name = 'farabi_admin'

urlpatterns = [
    path('login', log_in),
    path('logout', log_out),
    path('create-item', add_item),
    path('edit-item', edit_item),
    path('delete-item', delete_item),
    path('create-tag', add_tag),
    path('edit-tag', edit_tag),
    path('delete-tag', delete_tag),

]
