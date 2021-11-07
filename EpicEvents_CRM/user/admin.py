from django.contrib import admin
#from .models import User
from .models import TeamUser
# Register your models here.


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     """"""
#     ordering = ['role']
#     list_display = ('first_name', 'last_name', 'role', )
    
    
@admin.register(TeamUser)
class UserAdmin(admin.ModelAdmin):
    """"""
    #ordering = ['role']
    list_display = ('first_name', 'last_name', 'role', )