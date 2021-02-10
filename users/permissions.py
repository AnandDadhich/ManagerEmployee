from rest_framework import permissions
from .models import *


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        owner = UserInfo.objects.filter(email=request.user).first()
        print(owner)
        if owner!=None or request.user.is_superuser:
            return bool(request.user or request.user.is_superuser)