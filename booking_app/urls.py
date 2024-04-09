from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.book_table, name='booking-form'),
    path('booking-details/', views.booking_details, name='booking-details'),
]