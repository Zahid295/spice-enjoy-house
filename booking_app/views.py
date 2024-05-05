from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm
from .models import Table, Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
# views.py

def index(request):
    
    return render(request, 'base.html')

#def book_table(request):
#    table_names = ["Window View", "Cozy Corner", "Family Booth"]
#    form = BookingForm(initial={'table': table_names[0]})  # Set the default table name
#
#    if request.method != 'POST':
#        form = BookingForm()
#    else:
#        form = BookingForm(data=request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('booking_app:form')
#            
#    return render(request, 'booking_form.html', {'form': form})
@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data['table']
            booking_time = form.cleaned_data['booking_time']
            existing_booking = Booking.objects.filter(table=table, booking_time=booking_time).exists()
            if existing_booking:
                # show an error message
                return render(request, 'booking_app/booking_form.html', {'form': form, 'name_collection': Table.objects.all(), 'error_message': 'This table is already booked at the selected time.'})
            else:
                 form.instance.user = request.user
                 form.save()
            # Redirect to a valid URL (e.g., the booking success page)
                 return redirect('index')  # Update this to the actual URL
        else:
            if 'guest_name' in form.errors:
                messages.error(request, 'Guest name is too long')
            return render(request, 'booking_app/booking_form.html', {'form': form, 'name_collection': Table.objects.all()})

    else:
        form = BookingForm()

    name_collection = Table.objects.all()

    return render(request, 'booking_app/booking_form.html', {'form': form, 'name_collection': name_collection, 'confirmation_message': 'Booking successful!'})


def booking_details(request):
    print("Current user:", request.user)
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user)
        print("User bookings:", user_bookings) 
    else:
        user_bookings = None

    return render(request, 'booking_app/booking_details.html', {'user_bookings': user_bookings})
