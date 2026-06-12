from django.db import models

# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='rental_images/')
    image2 = models.ImageField(upload_to='rental_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='rental_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='rental_images/', null=True, blank=True)    
    image5 = models.ImageField(upload_to='rental_images/', null=True, blank=True)
    image6 = models.ImageField(upload_to='rental_images/', null=True, blank=True)
    image1_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image1_location = models.CharField(max_length=100, null=True, blank=True)
    image2_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image2_location = models.CharField(max_length=100, null=True, blank=True)               
    image3_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image3_location = models.CharField(max_length=100, null=True, blank=True)
    image4_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image4_location = models.CharField(max_length=100, null=True, blank=True)
    image5_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image5_location = models.CharField(max_length=100, null=True, blank=True)
    image6_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image6_location = models.CharField(max_length=100, null=True, blank=True)
    


