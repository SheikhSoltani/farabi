from django.contrib import admin

from .models import Item, Tag, Price

admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Price)
