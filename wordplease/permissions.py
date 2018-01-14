from django.utils import timezone
from rest_framework.permissions import BasePermission


class PostPermissions (BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' and obj.date<=timezone.now():
            return True
        return obj.user == request.user or request.user.is_superuser
