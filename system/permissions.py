from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_student


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_teacher


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
