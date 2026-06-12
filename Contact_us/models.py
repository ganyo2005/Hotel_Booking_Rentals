from django.db import models

# Create your models here.
class Contact_Us(models.Model):
    fullname = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    service_type = models.CharField(max_length=100, null=True, blank=True)
    about_business = models.TextField(null=True, blank=True)
    check_in_date = models.DateField(null=True, blank=True) 

    def __str__(self):
        return self.fullname    