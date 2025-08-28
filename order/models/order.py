from django.db import models
from django.contrib.auth.models import User

from product.models.product import Product


class Order(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
