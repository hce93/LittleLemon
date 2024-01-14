from .models import Menu, Booking
from rest_framework import serializers
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']