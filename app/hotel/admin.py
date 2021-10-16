from django.contrib import admin

from .models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created']