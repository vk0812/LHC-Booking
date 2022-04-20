from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data),
    path('day/<int:year>/<int:month>/<int:day>', views.for_a_day),
    path('deletebooking/<int:id>', views.delete_booking),
]
