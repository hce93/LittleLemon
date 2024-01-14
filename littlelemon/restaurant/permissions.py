from rest_framework import permissions

class ManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Manager').exists():
            return True
        return False