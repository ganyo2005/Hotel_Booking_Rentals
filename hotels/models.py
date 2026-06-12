from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
  
  
    image = models.ImageField(upload_to='hotel_images/')
    image2 = models.ImageField(upload_to='hotel_images/', null=True, blank=True) 
    image3 = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    image6 = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    image7 = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    image8 = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    image9 = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    image10 = models.ImageField(upload_to='hotel_images/', null=True, blank=True)





    
    room1_name = models.CharField(max_length=100, null=True, blank=True)
    room1_amenites= models.CharField(max_length=100, null=True, blank=True)
    room1_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    room2_name = models.CharField(max_length=100, null=True, blank=True)  
    room2_amenites= models.CharField(max_length=100, null=True, blank=True)
    room2_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    room3_name = models.CharField(max_length=100, null=True, blank=True)
    room3_amenites= models.CharField(max_length=100, null=True, blank=True)
    room3_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    room4_name = models.CharField(max_length=100, null=True, blank=True)      

    room4_amenites= models.CharField(max_length=100, null=True, blank=True)
    room4_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    room5_name = models.CharField(max_length=100, null=True, blank=True)  
    room5_amenites= models.CharField(max_length=100, null=True, blank=True)
    room5_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
      return self.name




    


