# import re
# from turtle import st
from django.shortcuts import render
from .models import Bookings
from .serializers import BookingsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def getDate(year, month, day):
    if(month >= 1 and month <= 9):
        if(day >= 1 and day <= 9):
            res = str(year)+"-0"+str(month)+"-0"+str(day)
        else:
            res = str(year)+"-0"+str(month)+"-"+str(day)
    else:
        if(day >= 1 and day <= 9):
            res = str(year)+"-"+str(month)+"-0"+str(day)
        else:
            res = str(year)+"-"+str(month)+"-"+str(day)
    return res


def validateTiming(start, end):
    if(start >= end):
        return False
    else:
        return True


def checkClash(dict_data):
    bookings = Bookings.objects.filter(
        date=dict_data['date'], venue=dict_data['venue'])
    serializer = BookingsSerializer(bookings, many=True)
    list_data = serializer.data
    for items in list_data:
        if(items['end_time'] > dict_data['start_time'] and dict_data['end_time'] > items['start_time']):
            return False  # Time Clash
    return True  # No Time Clash


@api_view(['GET'])
@csrf_exempt
def bookings(request):
    bookings = Bookings.objects.all()
    serializer = BookingsSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def book(request):
    if(validateTiming(request.data['start_time'], request.data['end_time']) == False):
        return Response("Start Time for the Event is after the End Time", status=status.HTTP_404_NOT_FOUND)

    if(checkClash(request.data) == False):
        return Response(f"{request.data['venue']} already booked during this time!!", status=status.HTTP_404_NOT_FOUND)

    serializer = BookingsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@csrf_exempt
def delete_booking(request, id):
    bookings = Bookings.objects.get(id=id)
    bookings.delete()
    return Response("Deleted")


@api_view(['GET'])
@csrf_exempt
def for_a_day(request, year, month, day):
    if request.method == 'GET':
        bookings = Bookings.objects.filter(date=getDate(year, month, day))
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
def for_a_venue(request, venue):
    if request.method == 'GET':
        bookings = Bookings.objects.filter(venue=venue)
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
