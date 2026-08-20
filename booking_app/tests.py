from datetime import date, time, timedelta

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import BookingForm
from .models import Booking, Table


class BookingAvailabilityTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='guest', password='password')
		self.table = Table.objects.create(name='Window View')
		self.other_tables = [
			Table.objects.create(name='Cozy Corner'),
			Table.objects.create(name='Family Booth'),
		]
		self.booking_date = date.today() + timedelta(days=1)

	def test_future_date_returns_half_hour_slots(self):
		response = self.client.get(
			reverse('available-times'),
			{'date': self.booking_date.isoformat()},
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()['times'][0]['value'], '09:00')
		self.assertEqual(response.json()['times'][-1]['value'], '21:30')

	def test_time_is_removed_when_all_tables_are_booked(self):
		for table in Table.objects.all():
			Booking.objects.create(
				table=table,
				user=self.user,
				guest_name='Guest',
				booking_date=self.booking_date,
				booking_time=time(19, 0),
			)

		response = self.client.get(
			reverse('available-times'),
			{'date': self.booking_date.isoformat()},
		)

		self.assertNotIn('19:00', {slot['value'] for slot in response.json()['times']})

	def test_form_rejects_an_existing_table_booking(self):
		Booking.objects.create(
			table=self.table,
			user=self.user,
			guest_name='Guest',
			booking_date=self.booking_date,
			booking_time=time(19, 0),
		)
		form = BookingForm(data={
			'table': self.table.pk,
			'guest_name': 'Another Guest',
			'booking_date': self.booking_date.isoformat(),
			'booking_time': '19:00',
		})

		self.assertFalse(form.is_valid())
		self.assertIn('booking_time', form.errors)
