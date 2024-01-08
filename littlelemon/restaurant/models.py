from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator

# Create your models here.

class Booking(models.Model):
    id = models.IntegerField(validators=[MaxValueValidator(limit_value=99999999999)], primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(limit_value=6)])
    reservation_slot = models.DateTimeField()

class Menu(models.Model):
    id = models.IntegerField(validators=[MaxValueValidator(limit_value=99999999999)], primary_key=True)
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10,decimal_places=2) 
    inventory = models.IntegerField(validators=[MaxValueValidator(limit_value=99999)]) 