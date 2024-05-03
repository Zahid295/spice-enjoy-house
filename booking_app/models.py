from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Table(models.Model):

    CHOICES = [
        ("Window View", "Window View"),
        ("Cozy Corner", "Cozy Corner"),
        ("Family Booth", "Family Booth"),
    ]
    name = models.CharField(max_length=50, choices=CHOICES, default="Window View", validators=[MinLengthValidator(1)])

    def __str__(self):
        return self.name

class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    guest_name = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    booking_date = models.DateField()
    booking_time = models.TimeField()
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):

        return f"{self.guest_name} at {self.table.name} on {self.booking_date} at {self.booking_time}"
