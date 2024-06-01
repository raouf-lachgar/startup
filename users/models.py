# users/models.py
from django.db import models
from django.contrib.auth.models import User

# users/models.py

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    STATE_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]
    state = models.CharField(max_length=4, choices=STATE_CHOICES)
    city = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

