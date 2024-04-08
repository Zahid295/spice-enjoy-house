from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm


# Create your views here.
# views.py

def index(request):
    
    return render(request, 'index.html')

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

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a valid URL (e.g., the booking success page)
            return redirect('')  # Update this to the actual URL
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})
