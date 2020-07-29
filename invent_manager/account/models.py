from django.db import models

# Create your models here.

class Account(models.Model):
    company = models.TextField(blank=True)
    number = models.IntegerField(blank=True)
    address = models.CharField(max_length=200, blank=True)


