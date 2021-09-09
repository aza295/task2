from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model


class Product(models.Model):

    name = models.CharField(max_length=50)
    title = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title