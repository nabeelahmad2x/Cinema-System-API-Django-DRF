from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'User'


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'Admin'


def admin_auth_required(func):
    def wrap(request, *args, **kwargs):
        if request.user.user_type == 'Admin':
            return func(request, *args, **kwargs)
        return Response({"Not Authorized to access. Only Admins allowed."}, status=status.HTTP_403_FORBIDDEN)

    return wrap
