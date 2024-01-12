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
import json
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from .forms import BookingForm

def sayHello(request):
 return HttpResponse('Hello World')

# def index(request):
#     return render(request, 'index.html',{})

def home(request):
    return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')



class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "menu.html"
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            # If the client accepts HTML, render the template
            return Response({'menu': response.data}, template_name='menu.html')
        return response
    
    
class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
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
    

def success(request):
    return render(request, 'success.html')
    
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})

@csrf_exempt
def bookings(request):
    # if request.method == 'POST':
    #     data = json.load(request)
    #     exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
    #         reservation_slot=data['reservation_slot']).exists()
    #     if exist==False:
    #         booking = Booking(
    #             first_name=data['first_name'],
    #             reservation_date=data['reservation_date'],
    #             reservation_slot=data['reservation_slot'],
    #         )
    #         booking.save()
    #     else:
    #         return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.filter(reservation_slot__date=date)

    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')