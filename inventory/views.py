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

    def create(self, request, *args, **kwargs):
        decoded_file = base64.b64decode(request.data['image'])
        # Generate file name:
        file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
        # Get the file name extension:
        file_extension = self.get_file_extension(file_name, decoded_file)

        complete_file_name = "%s.%s" % (file_name, file_extension,)

        image = ContentFile(decoded_file, name=complete_file_name)
        request_data = request.data.copy()
        request_data['image'] = image

        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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
