from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .forms import BookingForm, booking_time_choices
from .models import Table, Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Views

def index(request):
    
    return render(request, 'base.html')

def contact_us(request):
    return render(request, 'booking_app/contact_us.html')


def available_times(request):
    """Return valid restaurant slots for the selected date."""
    booking_date = request.GET.get('date')
    if not booking_date:
        return JsonResponse({'times': []})

    try:
        selected_date = timezone.datetime.strptime(booking_date, '%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({'error': 'Invalid date.'}, status=400)

    if selected_date < timezone.now().date():
        return JsonResponse({'times': []})

    table_id = request.GET.get('table')
    booked_query = Booking.objects.filter(
        booking_date=selected_date,
        is_cancelled=False,
    )
    if table_id and table_id.isdigit():
        booked_query = booked_query.filter(table_id=table_id)
    booked_times = list(booked_query.values_list('booking_time', flat=True))
    table_count = 1 if table_id else Table.objects.count()
    times = [
        {'value': value, 'label': label}
        for value, label in booking_time_choices(selected_date)
        if table_count and sum(1 for booked_time in booked_times if booked_time.strftime('%H:%M') == value) < table_count
    ]
    return JsonResponse({'times': times})


@login_required
def book_table(request):
    preselected_table = request.GET.get("table")
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data['table']
            booking_time = form.cleaned_data['booking_time']
            booking_date = form.cleaned_data['booking_date']
            existing_booking = Booking.objects.filter(
                table=table,
                booking_date=booking_date,
                booking_time=booking_time,
                is_cancelled=False,
            ).exists()
            if existing_booking:
                messages.error(request, "Oops! It looks like this table is already booked at the selected time. Please choose a different time or table.")
                return render(request, 'booking_app/booking_form.html', {'form': form})
            else:
                 form.instance.user = request.user
                 form.save()
                 messages.success(request, 'Booking successful!')
                 return redirect('booking-details')
        else:
            return render(request, 'booking_app/booking_form.html', {'form': form})

    else:
        form = BookingForm()

        if preselected_table:
            form.fields['table'].initial = preselected_table

    return render(request, 'booking_app/booking_form.html', {'form': form})

@login_required
def booking_details(request):
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user) 
    else:
        user_bookings = None

    today = timezone.now().date()

    return render(request, 'booking_app/booking_details.html', {'user_bookings': user_bookings, 'today': today})

@login_required
def edit_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if booking.booking_date < timezone.now().date():
        messages.error(request, "Past bookings cannot be edited.")
        return redirect('booking-details')
    if request.method != 'POST':
        form = BookingForm(instance=booking)
    else:
        form = BookingForm(instance=booking, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking-details')

    context = {'form': form, 'booking': booking}
    return render(request, 'booking_app/edit_booking.html', context)

@login_required
def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if booking.booking_date < timezone.now().date():
        messages.error(request, "Past bookings cannot be deleted.")
        return redirect('booking-details')
    if request.method == 'POST':
        booking.delete()
        return redirect('booking-details')

    context = {'booking': booking}
    return render(request, 'booking_app/delete_booking.html', context)

