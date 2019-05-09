from django.db import models

# Add your models here
class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

class Paitent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor)
    paitent=models.ForeignKey(Paitent)
    description = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    checked_in = models.DateTimeField(blank=True)
    time_seen = models.DateTimeField(blank=True)
