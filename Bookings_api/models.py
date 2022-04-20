from django.db import models


class Bookings(models.Model):
    event = models.CharField(verbose_name="Event",
                             max_length=100, default="Lecture")

    venue = models.CharField(verbose_name="Venue",
                             max_length=100)

    date = models.DateField(verbose_name="Date")

    start_time = models.TimeField(verbose_name="Starting Time")
    end_time = models.TimeField(verbose_name="Ending Time")

    def __str__(self):
        return self.event + ' ' + self.venue
