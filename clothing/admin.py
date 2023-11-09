from django.contrib import admin

# Register your models here.

from .models import Products, CartItems, Carts

admin.site.register(Products)
admin.site.register(CartItems)
admin.site.register(Carts)


