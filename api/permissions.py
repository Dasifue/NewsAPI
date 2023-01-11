from rest_framework import permissions


class ISAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author.id == request.user.id:
            return True
        return False
