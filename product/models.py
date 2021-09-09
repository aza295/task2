from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model

class Product:
    name = models.CharField(max_length=50)
    title = models.TextField()
    price = models.DecimalField(max_digits=10)

    def __str__(self):
        return self.title