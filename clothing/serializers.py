from rest_framework import serializers

from .models import Products, CartItems, Carts

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = '__all__'