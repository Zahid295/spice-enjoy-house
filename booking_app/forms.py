from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, time, timedelta
from .models import Booking, Table


SERVICE_START = time(9, 0)
SERVICE_END = time(22, 0)
SLOT_MINUTES = 30


def booking_time_choices(selected_date=None):
    choices = []
    current = datetime.combine(timezone.now().date(), SERVICE_START)
    end = datetime.combine(timezone.now().date(), SERVICE_END)
    current_time = timezone.localtime().time().replace(second=0, microsecond=0)
    while current < end:
        slot = current.time()
        if selected_date != timezone.now().date() or slot > current_time:
            choices.append((slot.strftime('%H:%M'), slot.strftime('%I:%M %p').lstrip('0')))
        current += timedelta(minutes=SLOT_MINUTES)
    return choices


class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(queryset=Table.objects.all(), empty_label="Select a table")
    guest_name = forms.CharField(max_length=100)
    booking_date = forms.DateField(
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={
                'class': 'form-input',
                'type': 'date',
                'min': timezone.now().date().isoformat(),
            },
        )
    )
    booking_time = forms.TypedChoiceField(
        choices=booking_time_choices,
        coerce=lambda value: datetime.strptime(value, '%H:%M').time(),
        empty_value=None,
        widget=forms.Select(attrs={'class': 'form-input'}),
    )

    class Meta:
        model = Booking
        fields = ('table', 'guest_name', 'booking_date', 'booking_time')

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date and booking_date < timezone.now().date():
            raise ValidationError("Booking date cannot be in the past.")
        return booking_date

    def clean_guest_name(self):
        guest_name = self.cleaned_data.get('guest_name')
        if len(guest_name) > 15:
            raise forms.ValidationError("Guest name is too long")
        return guest_name

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        booking_date = self.cleaned_data.get('booking_date')
        if booking_time and booking_time.strftime('%H:%M') not in dict(booking_time_choices(booking_date)):
            raise ValidationError("Please select one of the available booking times.")
        return booking_time

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get('table')
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')
        conflicting_bookings = Booking.objects.filter(
                table=table,
                booking_date=booking_date,
                booking_time=booking_time,
                is_cancelled=False,
            )
        if self.instance.pk:
            conflicting_bookings = conflicting_bookings.exclude(pk=self.instance.pk)
        if table and booking_date and booking_time and conflicting_bookings.exists():
            self.add_error('booking_time', 'This table is already booked at that time. Please choose another time.')
        return cleaned_data
