from rest_framework.permissions import BasePermission


class IsCustomAdminUser(BasePermission):
    """
    Custom IsAdminUser permission that looks on the `role`
    instead in the `is_staff` field.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'
