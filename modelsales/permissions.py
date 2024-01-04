from rest_framework import permissions


class IsActiveEmployeePermission(permissions.BasePermission):
    """
    Пользователь может иметь доступ, только если он активен.
    """

    def has_permission(self, request, view):
        return request.user.is_active
