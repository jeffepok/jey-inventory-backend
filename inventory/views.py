import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from inventory.models import Item
from inventory.serializers import ItemSerializer, CategorySerializer
from rest_framework import generics, permissions
from inventory.permissions import IsOwnerOrAdmin
from django.core.files.base import ContentFile
import base64
from rest_framework import status


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user)


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


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'inventory': reverse('item-list', request=request, format=format)
    })
