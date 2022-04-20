import re
from turtle import st
from django.shortcuts import render
from .models import Bookings
from .serializers import BookingsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
@csrf_exempt
def data(request):
    if request.method == 'GET':
        bookings = Bookings.objects.all()
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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
        bookings = Bookings.objects.filter(date=res)
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data)
