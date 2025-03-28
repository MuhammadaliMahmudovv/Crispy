from django.db import models
from django.utils.timezone import now

class reservation(models.Model):
    full_name = models.CharField(max_length=255)
    email_adress = models.EmailField(max_length=255)
    phone_number = models.IntegerField(max_length=255)
    number_of_persons = models.IntegerField(max_length=255)
    date = models.DateField()
    time = models.TimeField(default=now)
    text = models.TextField(max_length=255)