from rest_framework import permissions
from .models import *


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        owner = Manager.objects.filter(emp_user__email=request.user).first()
        if owner:
            return bool(request.user or request.user.is_superuser)
