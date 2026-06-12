from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from rentals.models import Rental


class Renting(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rent = models.ForeignKey(
        Rental,
        on_delete=models.CASCADE
    )

    item = models.CharField(
        max_length=20,
       null=True
    )
    destination = models.CharField(
        max_length=100,
        null=True
    )
    price = models.DecimalField(    
        max_digits=10,
        decimal_places=2,
        null=True
    )
    total_price = models.DecimalField(
        max_digits=10,  
        decimal_places=2,
        null=True
    )

    check_in = models.DateField()

    check_out = models.DateField()

    quantity = models.IntegerField(null=True, default=1)

    # total_price = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2
    # )

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

        return f"{self.user.username} - {self.rent.name}"