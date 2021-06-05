from django.shortcuts import render

from .models import *

def categories(request):
    return(
        {'categories':Category.objects.all()}
    )

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html',{'products':products})
    