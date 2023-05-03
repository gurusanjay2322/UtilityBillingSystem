import email
import re
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Details(models.Model):
    cus_id = models.IntegerField()
    Name = models.CharField(max_length=120, default="", null=False)
    bill = models.IntegerField()






class contact(models.Model):

    name = models.CharField(max_length=45)
    email = models.EmailField()
    # phone=models.CharField(max_length=10)
    message = models.TextField()






