from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.book_table, name='booking-form'),
    path('booking-details/', views.booking_details, name='booking-details'),
    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit-booking'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete-booking'),
]