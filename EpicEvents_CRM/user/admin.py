from django.contrib import admin
from django import forms

from .models import TeamUser, Team


# Register your models here.
class TeamUserForm(forms.ModelForm):
    """ change admin interface"""
    class Meta:
        fields = ('username','first_name', 'last_name', 'email', 'password', 'role', 'is_staff' )


@admin.register(TeamUser)
class TeamUserAdmin(admin.ModelAdmin):
    """"""
    ordering = ['role']
    list_display = ('username','first_name', 'last_name', 'email', 'role', 'id', 'is_staff')
    #form = TeamUserForm


admin.site.register(Team)