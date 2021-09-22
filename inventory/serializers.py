from rest_framework import serializers
from inventory.models import Item, Category


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category', 'image', 'price', 'owner']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
