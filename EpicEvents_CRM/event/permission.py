from rest_framework import permissions


class EventPermission(permissions.BasePermission):
    """ allow permission for crud"""
    
    def has_permission(self, request, view):
        user_team = request.user.role.role 
        if user_team == 'sales':
            return True
        elif user_team == 'support':
            return request.method in ['GET', 'PUT']
        else:
            return True 
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user
        elif request.method in ['PUT', 'PATCH','DELETE']:
            return request.user == obj.support_contact
        else:
            return False