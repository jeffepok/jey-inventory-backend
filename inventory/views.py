from django.shortcuts import render

# Create your views here.

from inventory.models import Item, Category
from inventory.serializers import ItemSerializer, CategorySerializer
from rest_framework import generics, permissions
from inventory.permissions import IsOwnerOrAdmin

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
       return Item.objects.filter(owner = self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]


class CategoryList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = CategorySerializer