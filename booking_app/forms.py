from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, Table

class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(queryset=Table.objects.all(), empty_label="Select a table")
    guest_name = forms.CharField(max_length=100)

    class Meta:
        model = Booking
        fields = ('table', 'guest_name', 'booking_date', 'booking_time')

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date and booking_date < timezone.now().date():
            raise ValidationError("Booking date must be in the future.")
        return booking_date

    def clean_guest_name(self):
        guest_name = self.cleaned_data.get('guest_name')
        if len(guest_name) > 15:
            raise forms.ValidationError("Guest name is too long")
        return guest_name
