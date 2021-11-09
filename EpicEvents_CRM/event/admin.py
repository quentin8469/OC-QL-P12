from django.contrib import admin
from .models import Event, EventStatus
# Register your models here.


admin.site.register(EventStatus)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """"""
    list_display = ('client', 'even_date', 'support_contact','event_status')
    list_filter = ('client', 'even_date',)
    
