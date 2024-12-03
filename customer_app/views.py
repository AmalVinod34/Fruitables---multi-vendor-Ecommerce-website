from django.shortcuts import render,redirect
from app.models import User
from .models import *
from seller_app.models import Product
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def customer_home(request):
    se = request.session['sid']
    cu_se = User.objects.get(id=se)
    card = Product.objects.all()
    return render(request,"customer/customer_home.html",{"card":card,"data":cu_se})

def customer_shop(request):
    card = Product.objects.all()
    return render(request,"customer/shop.html",{"card":card})

def customer_cart(request):
    user_session = request.session['sid']
    user_id = User.objects.get(id=user_session)
    customer = Customer.objects.get(customer_id=user_id)
    cart = Cart.objects.filter(customer_id=customer.id)
    return render(request,"customer/cart.html",{"product":cart})

def customer_checkout(request):
    return render(request,"customer/checkout.html")

def customer_contact(request):
    return render(request,"customer/contact.html")

def edit(request):
    x = request.session['sid']
    user = User.objects.get(id=x)
    customer = Customer.objects.get(customer_id=user)
    return render(request,"customer/edit.html",{"data":user,"val":customer})

def update(request,u_id,c_id):
    if request.method=='POST':
        name=request.POST.get("name")
        emali=request.POST.get("email")
        phone=request.POST.get("phone")
        user=request.POST.get("username")
        password=request.POST["password"]

        old_user=User.objects.get(id=u_id)
        old_user.first_name=name
        old_user.email=emali
        old_user.username=user
        old_user.password=password

        old_cust=Customer.objects.get(id=c_id)
        old_cust.Name=name
        old_cust.Email=emali
        old_cust.Phone=phone
        old_cust.Username=user
        old_cust.Password=password
        
        old_cust.save()
        old_user.save()
        return redirect(customer_home)
    else:
        return redirect(edit)
 
def add_to_cart(request,id):
    if request.method=='POST':
        user_session = request.session['sid']
        user_id = User.objects.get(id=user_session)
        customer = Customer.objects.get(customer_id=user_id)
        product = Product.objects.get(id=id)
        quantity = int(request.POST['Quantity'])
        ordered_item,created = Cart.objects.get_or_create(seller_id=product.seller_id,customer_id=customer.id,Title=product.Title,Image=product.Image,Price=product.Price)
        if created:
            ordered_item.Quantity = quantity
            ordered_item.save()
        else:
            ordered_item.Quantity+=quantity
            ordered_item.save()
        add_to_order,created_ = Order.objects.get_or_create(seller_id=product.seller_id,product_id=product.id,customer_id=ordered_item.customer_id,product_name=product.Title,product_image=product.Image,order_status="CART STAGE")
        if created_:
            add_to_order.product_quantity = quantity
            add_to_order.Total=product.Price*quantity
            add_to_order.save()
        else:
            add_to_order.product_quantity+=quantity
            add_to_order.Total+=product.Price*quantity
            add_to_order.save()
        return redirect(customer_cart)
    else:
        return redirect(customer_shop)
    
def remove_from_cart(request,id):
    item = Cart.objects.get(id=id)
    order_item = Order.objects.get(id=item.id)
    item.delete()
    order_item.delete()
    return redirect(customer_cart)

def checkout(request):
    user_session = request.session['sid']
    user_id = User.objects.get(id=user_session)
    customer = Customer.objects.get(customer_id=user_id)
    cart = Cart.objects.filter(customer_id=customer.id)
    return render(request,"customer/checkout.html",{"items":cart,"user":customer})

def order(request,id):
    if request.method=='POST':
        product = Cart.objects.filter(customer_id=id)
        customer_ = Customer.objects.get(id=id)
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        create_order = Order.objects.filter(customer_id=customer_.id).update(Name=name,Phone=phone,Email=email,Address=address,order_status="ORDER PLACED")
        product.delete()
        success_message = " Order placed. Continue shopping..."
        messages.success(request,success_message)
        return redirect(customer_home)
    else:
        return redirect(checkout)

def order_details(request):
    user_session = request.session['sid']
    user_id = User.objects.get(id=user_session)
    customer = Customer.objects.get(customer_id=user_id)
    cart = Order.objects.filter(customer_id=customer.id).exclude(order_status="CART STAGE")    
    return render(request,"customer/order_details.html",{"order":cart})