from rest_framework import serializers
from .models import Item, Tag, Price


class ItemSerializer(serializers.ModelSerializer):
    price_serialized = serializers.SerializerMethodField('price_serializer')
    tag_serialized = serializers.SerializerMethodField('tag_serializer')

    class Meta:
        model = Item
        fields = ('id', 'name', 'image', 'slug', 'description', 'purpose', 'color',
                  'degree_of_gloss', 'warranty', 'expiration_date', 'composition',
                  'method_of_use', 'expense', 'flammable', 'traits', 'price_serialized', 'tag_serialized')


    def price_serializer(self, obj):
        return PriceSerializer(obj.price, many=True).data

    def tag_serializer(self, obj):
        return TagSerializer(obj.tag).data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'