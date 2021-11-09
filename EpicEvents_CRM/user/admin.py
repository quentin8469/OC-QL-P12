from django.contrib import admin
from django import forms

from .models import TeamUser, Team


# Register your models here.
class TeamUserForm(forms.ModelForm):
    """ change admin interface"""
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'password', 'role', )


@admin.register(TeamUser)
class TeamUserAdmin(admin.ModelAdmin):
    """"""
    ordering = ['role']
    list_display = ('first_name', 'last_name', 'email', 'role', 'id' )
    form = TeamUserForm


admin.site.register(Team)