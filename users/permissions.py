from rest_framework.permissions import BasePermission


class UsersPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST" or request.user.is_superuser:
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

       return request.user == obj or request.user.is_superuser