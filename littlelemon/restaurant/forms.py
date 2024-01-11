from django import forms
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(forms.ModelForm):
    no_of_guests = forms.ChoiceField(
        choices=[('', 'Select Guests')] + [(i, str(i)) for i in range(1, 9)],
        label='Number of Guests',
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    reservation_slot = forms.DateTimeField(
        label='Reservation Slot',
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],  # Adjust the format based on your needs
    )
    
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'reservation_slot']
        
