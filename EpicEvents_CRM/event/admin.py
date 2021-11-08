from django.contrib import admin
from .models import Event
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """"""
    list_display = ('client', 'even_date', 'support_contact','event_status')
    list_filter = ('client', 'even_date',)