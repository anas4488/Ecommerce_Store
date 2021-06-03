from django.shortcuts import render

from .models import *

def all_products(request):
    products = Product.objects.all()
