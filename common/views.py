from django.shortcuts import redirect, render

from common.models import Customer, Seller


# Create your views here.
def index(request):
    return render(request, 'common/index.html')

def customer_signup(request):
    msg = ''

    if request.method == 'POST':
        customer_name = request.POST["cname"]
        customer_email = request.POST["cemail"]
        customer_number = request.POST["cnumber"]
        customer_password = request.POST["cpassword"]
        
        try:
            new_customer = Customer(
                c_name = customer_name,
                c_email = customer_email,
                c_phone = customer_number,
                c_password = customer_password            
            )
            new_customer.save()
            msg = 'succesfully registered'
        except:
            msg = 'invalid data'


    return render(request, 'common/customer_signup.html', {'message': msg})

def customer_login(request):
    msg = ''

    if request.method == 'POST':
        customer_username = request.POST["cname"]
        customer_password = request.POST["cpassword"]
        
        try:
            customer = Customer.objects.get(        
                c_email = customer_username,
                c_password = customer_password            
            )
            request.session['customer'] = customer.id
            return redirect('customer:home')
        except:
            msg = 'invalid username or password'


    return render(request, 'common/customer_login.html', {'message': msg})

def seller_signup(request):
    msg = ''

    if request.method == 'POST':
        seller_name = request.POST["cname"]
        seller_email = request.POST["cemail"]
        seller_number = request.POST["cnumber"]
        seller_password = request.POST["cpassword"]
        
       # try:
        new_seller = Seller(
            s_name = seller_name,
            s_email = seller_email,
            s_phone = seller_number,
            s_password = seller_password            
        )
        new_seller.save()
        msg = 'succesfully registered'
       # except:
            # msg = 'invalid data'


    return render(request, 'common/seller_signup.html', {'message': msg})

def seller_login(request):
    msg = ''

    if request.method == 'POST':
        seller_username = request.POST["cname"]
        seller_password = request.POST["cpassword"]
        
        # try:
        seller = Seller.objects.get(        
            s_email = seller_username,
            s_password = seller_password            
        )
        request.session['seller'] = seller.id
        return redirect('seller:home')
        # except:
        #     msg = 'invalid username or password'


    return render(request, 'common/seller_login.html', {'message': msg})