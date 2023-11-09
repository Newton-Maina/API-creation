from django.shortcuts import render

# Create your views here.

from .models import Products, CartItems, Carts

from .serializers import ProductSerializer, CartItemSerializer, CartSerializer

from rest_framework import viewsets

class ProductView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CartItemView(viewsets.ModelViewSet):
    queryset = CartItems.objects.all()
    serializer_class = CartItemSerializer

class CartView(viewsets.ModelViewSet):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer