from django.contrib import admin

from .models import Client

#Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """"""
    list_display = ('company_name', 'first_name', 'last_name', 'email', 'sales_contact', )
    list_filter = ("sales_contact",)