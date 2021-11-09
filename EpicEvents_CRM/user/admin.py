from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import TeamUser, Team


# Register your models here.

admin.site.register(UserAdmin, Team)


@admin.register(TeamUser)
class TeamUserAdmin(admin.ModelAdmin):
    """"""
    #ordering = ['role']
    list_display = ('__str__', 'id' )

