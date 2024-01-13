from django import forms
from .models import Booking
from datetime import date


# Code added for loading form data on the Booking page
class BookingForm(forms.ModelForm):
    no_of_guests = forms.ChoiceField(
        choices=[('', 'Select Guests')] + [(i, str(i)) for i in range(1, 7)],
        label='Number of Guests',
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    reservation_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    reservation_time = forms.ChoiceField(
        choices = [(f"{h:02d}:{m:02d}", f"{h:02d}:{m:02d}") for h in range(11, 22) for m in range(0, 60, 30)],
        label='Reservation Time',
        widget=forms.Select(attrs={'class': 'form-control'}))
    
    # reservation_slot = forms.DateTimeField(
    #     label='Reservation Slot',
    #     widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
    #     input_formats=['%Y-%m-%dT%H:%M'],  # Adjust the format based on your needs
    # )
    
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'reservation_date', 'reservation_time']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value for my_date_field
        self.fields['reservation_date'].initial = date.today()
        
