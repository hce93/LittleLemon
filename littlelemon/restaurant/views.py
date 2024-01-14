from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import datetime
from django.core import serializers
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
import json
from .serializers import MenuSerializer, BookingSerializer, ManagerSerializer
from .models import Menu, Booking
from .forms import BookingForm
from .permissions import ManagerPermission

def sayHello(request):
 return HttpResponse('Hello World')

# def index(request):
#     return render(request, 'index.html',{})

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return render(request, 'menu.html', {'menu': serializer.data})
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[ManagerPermission]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingFormView(FormView):
    template_name = 'book.html'
    form_class = BookingForm
    success_url = 'success/'
    
    def form_valid(self, form):
        
        booking_instance = form.save(commit=False)

        # Create the reservation_slot attribute based on reservation_date and reservation_time
        reservation_date = form.cleaned_data['reservation_date']
        reservation_time = datetime.strptime(form.cleaned_data['reservation_time'], '%H:%M').time()
        reservation_slot = datetime.combine(reservation_date, reservation_time)

        # Assign the calculated reservation_slot to the booking_instance
        booking_instance.reservation_slot = reservation_slot

        # Save the form instance to the model
        booking_instance.save()
        
        return super().form_valid(form)


class BookingViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes=[ManagerPermission]
    

def success(request):
    return render(request, 'success.html')

class AddManager(generics.ListAPIView):
    permission_classes=[ManagerPermission]
    queryset = User.objects.filter(groups__name="Manager")
    serializer_class = ManagerSerializer
    
    def post(self, request, *args, **kwargs):
        user = User.objects.all().get(username = request.data.get('username'))
        manager_group = Group.objects.get(name="Manager")
        user.groups.add(manager_group)
        user.save()
        return Response(self.get_serializer(user).data)
    
    def destroy(self, request, *args, **kwargs):
        manager_group = Group.objects.get(name="Manager")
        user = User.objects.all().get(username = request.data.get('username'))
        user.groups.remove(manager_group)
        user.save()
        return Response(self.get_serializer(user).data)
    
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})

@csrf_exempt
def bookings(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.filter(reservation_slot__date=date)

    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')