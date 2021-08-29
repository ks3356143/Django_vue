from rest_framework.permissions import BasePermission
from .models import Project

SAFE_METHODS = ('GET','HEAD','OPTIONS')

class IsSpecifiedProjectOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj._meta.object_name == "Project":
            project_id = obj.id
        else:
            project_id = obj.project_id
        allow_owners = []
        for o in Project.objects.filter(id=project_id)[0].owner.values():
            allow_owners.append(o['id'])
        return bool(
            request.methods in SAFE_METHODS or
            request.user and
            request.user.id in allow_owners or
            request.user.is_superuser
        )