from django.db import models
from django.conf import settings
from apps.catalog.models import Product

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} ({self.user or self.session_key})"

    @property
    def total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())

class CartItem(models.Model):
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, default='M')
    price = models.DecimalField(max_digits=10, decimal_places=2)  # snapshot at time of adding

    def __str__(self):
        return f"{self.quantity}x {self.product.name} ({self.size})"

    @property
    def total_price(self):
        return self.quantity * self.price
