from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# views.py

def index(request):
    # Any additional context data you want to pass to index.html
    context = {
        'welcome_message': 'Welcome to our restaurant!',  # Example context variable
    }
    return render(request, 'index.html', context)

