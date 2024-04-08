from django import forms
from .models import Booking, Table

class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(queryset=Table.objects.all(), empty_label="Select a table")

    class Meta:
        model = Booking
        fields = ('table', 'guest_name', 'booking_date', 'booking_time')