from django.contrib import admin
from .models import Bookings


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('event', 'venue', 'date', 'start_time', 'end_time')
