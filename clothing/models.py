from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='Description')
    image_url = models.ImageField(upload_to='images', default='product.jpg')

    def __str__(self):
        return self.name

class CartItems(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Carts(models.Model):
    products = models.OneToOneField(Products, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItems)

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.product.price * item.quantity

        return total
