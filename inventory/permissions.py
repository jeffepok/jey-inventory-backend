from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to read and edit it.
    Admin has unlimited permissions
    """

    def has_object_permission(self, request, view, obj):
        # Read or write permissions are only allowed to admin
        if request.user.is_superuser:
            return True

        # Read or Write permissions are allowed to the owner of the item.
        return obj.owner == request.user
