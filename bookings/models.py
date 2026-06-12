from django.db import models
from django.contrib.auth.models import User
from hotels.models import Hotel
from hotels.models import Hotel

class Hotel_Booking(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )


    user = models.CharField(max_length=40,null=True)

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE
    )

    room_type = models.CharField(
        max_length=20,
        null=True
    )

    check_in = models.DateField()

    check_out = models.DateField()

    guests = models.IntegerField(default=1)

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    agent_name=models.CharField(max_length=100,default='Ahmed Alhaj')
    agent_number=models.CharField(max_length=10,default='0595407164')
    customer_number=models.CharField(max_length=10,null=True)


    def __str__(self):

        return f"{self.user} - {self.hotel.name}"