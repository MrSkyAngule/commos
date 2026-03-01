from django.contrib import admin

from commo.models import Commo


@admin.register(Commo)
class CommoAdmin(admin.ModelAdmin):
    list_display = ('data', 'created_at', 'device_id')