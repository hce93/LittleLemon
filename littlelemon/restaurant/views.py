from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking

def sayHello(request):
 return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html',{})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer 
    