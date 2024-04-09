from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Table(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.guest_name} at {self.table} on {self.booking_date}"
