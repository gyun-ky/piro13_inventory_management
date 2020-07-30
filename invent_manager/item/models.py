from django.db import models
# Create your models here.

class Account(models.Model):
    company = models.TextField(blank=True)
    number = models.IntegerField(blank=True)
    address = models.CharField(max_length=200, blank=True)

class Item(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name="상품명")
    image = models.ImageField(blank=True, upload_to="item/image", verbose_name="이미지")
    content = models.TextField(blank=True, verbose_name="내용")
    price = models.IntegerField(verbose_name="가격")
    amount = models.IntegerField(verbose_name="수량")
    account = models.ManyToManyField('Account')