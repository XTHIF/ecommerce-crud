from django.shortcuts import render

from common.models import Product

def customerhome(request):
    return render(request, 'customer/home.html')

def viewproduct(request):
    return render(request, 'seller/viewproduct.html')