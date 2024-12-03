from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User
from customer_app.models import Customer
from seller_app.models import Seller,Product
from customer_app.views import customer_home
from seller_app.views import seller_home

# Create your views here.

def index(request):
    card = Product.objects.all()
    customers = Customer.objects.all()
    c_num = 0
    for j in customers:
        c_num+=1
    num = 0
    for i in card:
        num+=1
    return render(request,"index.html",{"card":card,"num":num,"c_num":c_num})

def shop(request):
    card = Product.objects.all()
    return render(request,"shop.html",{"card":card})

def contact(request):
    return render(request,"contact.html")

def admin_home(request):
    return render(request,"admin_home.html")

def user_register(request):
    if request.method=='POST':
        try:
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            username=request.POST['username']
            password=request.POST['password']
            user_save= User.objects.create_user(first_name=name,email=email,username=username,password=password,user_type="customer")
            customer_save=Customer.objects.create(Name=name,Email=email,Phone=phone,Username=username,Password=password,customer=user_save)
            customer_save.save()
            return redirect(us_login)
        except Exception as e:
            error_message = "Username already exists or Invalid details !"
            messages.error(request,error_message)
            return render(request,"customer/user_register.html")
    else: 
        return render(request,"customer/user_register.html")

def seller_register(request):
    if request.method=='POST':
        try:
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            username=request.POST['user']
            password=request.POST['pass']
            user_save= User.objects.create_user(first_name=name,email=email,username=username,password=password,user_type="seller",approve_seller="waiting")
            seller_save=Seller.objects.create(Name=name,Email=email,Phone=phone,Username=username,Password=password,seller=user_save)
            seller_save.save()
            return redirect(us_login)
        except Exception as e:
            error_message = "Username already exists or Invalid details !"
            messages.error(request,error_message)
            return render(request,"seller/seller_register.html")
    else: 
        return render(request,"seller/seller_register.html")
    
def approve(request):
    u = User.objects.filter(approve_seller="waiting")
    return render(request,"approve.html",{"data":u})

def approve_seller(request,id):
    User.objects.filter(id=id).update(approve_seller="approved")
    return redirect(approve)

def reject_approval(request,id):
    seller = Seller.objects.get(seller_id=id)
    seller.delete()
    return redirect(approve)

def us_login(request):
    if request.method=='POST':
        em=request.POST['user']
        pwd=request.POST['pass']
        x=authenticate(request,username=em,password=pwd)
        if x is not None and x.is_superuser==1:
            login(request,x)
            request.session['aid']=x.id
            return render(request,"admin_home.html")
        elif x is not None and x.user_type=="customer":
            login(request,x)
            request.session['sid']=x.id
            return redirect(customer_home)
        elif x is not None and x.approve_seller=="approved":
            login(request,x)
            request.session['tid']=x.id
            return redirect(seller_home)
        elif x is not None and x.approve_seller=="waiting":
            error_message = "Your approval for Bussiness account is pending !"
            messages.error(request,error_message)
            return render(request,"login.html")
        else:
            error_message = " Invalid username or password !"
            messages.error(request,error_message)
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    
def us_logout(request):
    logout(request)
    return redirect(index)

def view_customer(request):
    x = User.objects.filter(user_type="customer")
    return render(request,"view_customer.html",{"data":x})

def view_seller(request):
    x = User.objects.filter(user_type="seller")
    c = Seller.objects.all()
    return render(request,"view_seller.html",{"data":x,"val":c})

def login_req(request):
    error_message = "Please login with your account for buy products !"
    messages.error(request,error_message)
    return redirect(shop)