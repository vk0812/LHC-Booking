from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.bookings),
    path('book/', views.book),
    path('day/<int:year>/<int:month>/<int:day>', views.for_a_day),
    path('venue/<str:venue>', views.for_a_venue),
    path('deletebooking/<int:id>', views.delete_booking),
]
