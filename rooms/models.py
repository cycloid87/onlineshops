from django.db import models
from django.urls import reverse
from shop.models import Category


class Rooms(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    # user_address = models.CharField(max_length=200)
    # user_number = models.CharField(max_length=200)
    # user_food = models.CharField(max_length=200)
    # contents = models.TextField()