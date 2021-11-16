from rest_framework import permissions


class ContractPermission(permissions.BasePermission):
    """ allow permission for crud"""
    
    def has_permission(self, request, view):
        user_team = request.user.role.role 
        if user_team == 'sales':
            return True
        elif user_team == 'support':
            return False
        else:
            return True
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user
        elif request.method in ['PUT', 'PATCH']:
            return request.user == obj.sales_contact
        else:
            return False