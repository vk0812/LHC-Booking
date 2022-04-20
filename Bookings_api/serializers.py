from rest_framework import serializers
from .models import Bookings


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ['id', 'event', 'venue', 'date', 'start_time', 'end_time']
        # fields = '__all__'
