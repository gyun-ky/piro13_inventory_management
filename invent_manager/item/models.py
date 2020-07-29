from django.db import models

# Create your models here.

class item(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    # account =
