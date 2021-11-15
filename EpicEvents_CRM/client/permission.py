from rest_framework import permissions


class ClientPermission(permissions.BasePermission):
    """ allow permission for crud"""
    
    def has_permission(self, request, view):
        # si je suis sales_contact et que je m'occupe du client read ok
        # si je suis manager read ok
        # si je suis support et que je m'occupe de l'event du client read ok
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user == obj.sales_contact
        elif request.method in ['PUT', 'PATCH']:
            return request.user == obj.sales_contact 