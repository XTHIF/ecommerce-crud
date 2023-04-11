from itertools import product
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from common.models import Product

def sellerhome(request):
    return render(request, 'seller/home.html')

def viewproduct(request):
    product = Product.objects.filter(m_Seller_id = request.session['seller'])
    return render(request, 'seller/viewproduct.html', {'products': product})

def addproduct(request):
    msg=''
    if request.method == 'POST':
        productname = request.POST['pname']
        description = request.POST['description']
        product_in_stock = request.POST['stock left']       
        product_price = request.POST['price']
        category = request.POST['category']
        image = request.FILES['pimage']

        product = Product(m_name = productname,                         
                          m_price = product_price,                          
                          m_description = description,
                        m_Seller_id = request.session['seller'],
                        m_category = category,
                        images = image)
        product.save()
        msg = 'product succesfully added'

    return render(request,'seller/addproduct.html',{'message':msg})

def updateproduct(request):
    msg = ''
    products = Product.objects.filter(m_Seller_id = request.session['seller'])
    if request.method == 'POST':
        pid = request.POST['product']
        productname = request.POST['pname']
        description = request.POST['description']
        # product_in_stock = request.POST['stock left']       
        product_price = request.POST['price']
        # category = request.POST['category']

        product = Product.objects.get(id = pid)
        product.m_name = productname
        product.m_description = description
        product.m_price = product_price
        product.save()
        msg ='update successful'

    return render(request, 'seller/updateproduct.html',{'products': products, 'message':msg})

def getproduct(request):
     pid = request.POST['id'] 

     product = Product.objects.get(id = pid)
     data = [{'m_name':product.m_name,'m_price':product.m_price,'m_description':product.m_description }]  
     return JsonResponse({'data':data})

def delete_product(request,p_id):
    product = Product.objects.get(id=p_id)
    product.delete()
    msg='deleted succesfully'
    product = Product.objects.filter(m_Seller_id = request.session['seller'])
    return render(request, 'seller/viewproduct.html', {'products': product,'message':msg})

def viewpage(request,p_id):
    product = Product.objects.get(id=p_id)
    return render(request, 'seller/viewpage.html', {'products': product})

@api_view(['GET'])
def index(request):
    message = 'congratulations...... you have created an API'
    return Response(message)

@api_view(['GET'])
def number(request):
    message = 10
    return Response(message)

