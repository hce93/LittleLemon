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
        # This method is called when the form is successfully validated.
        # Save the form data to the model here.
        booking = form.save()  # This will automatically save the form data to the Booking model
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