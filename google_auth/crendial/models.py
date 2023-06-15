from django.db import models

# Create your models here.
class EmailMobileUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
