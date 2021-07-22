from django.contrib import admin
from .models import Wilaya, Commune
# Register your models here.

@admin.register(Wilaya)
class WilayaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','price' ,'active']
    list_display_links =('id', 'name')
    list_filter = ['active']
    list_editable = ['price']
    list_per_page = 30


@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links =('id', 'name')
    list_per_page = 30

