from django.shortcuts import render,redirect
from app.models import User
from .models import *
from .forms import ProductForm
from customer_app.models import Order
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

def seller_home(request):
    se = request.session['tid']
    se_se = User.objects.get(id=se)
    return render(request,"seller/seller_home.html",{"data":se_se})

def seller_contact(request):
    return render(request,"seller/contact.html")

def seller_edit(request):
    x = request.session['tid']
    user = User.objects.get(id=x)
    customer = Seller.objects.get(seller_id=user)
    return render(request,"seller/edit.html",{"data":user,"val":customer})

def seller_update(request,u_id,s_id):
    if request.method=='POST':
        name=request.POST.get("name")
        emali=request.POST.get("email")
        phone=request.POST.get("phone")
        username=request.POST.get("username")
        password=request.POST["password"]
        upd_user=User.objects.filter(id=u_id).update(first_name=name,email=emali,username=username,password=password)
        upd_sell=Seller.objects.filter(id=s_id).update(Name=name,Email=emali,Phone=phone,Username=username,Password=password)
        return redirect(seller_home)
    else:
        return redirect(seller_edit)
    
def add_product(request):
    if request.method=='POST':
        x = ProductForm(request.POST,request.FILES)
        session = request.session['tid']
        se = User.objects.get(id=session)
        seller_ = Seller.objects.get(seller_id=se)
        if x.is_valid():
            prod = x.save(commit=False)
            prod.seller_id = seller_.id
            prod.save()
            return redirect(view_product)
        else:
            return redirect(add_product)
    else:
        product_form = ProductForm()
        return render(request,"seller/add_product.html",{"data":product_form})
    
def view_product(request):
    session = request.session['tid']
    user_id = User.objects.get(id=session)
    seller_session = Seller.objects.get(seller_id=user_id)
    product_id = Product.objects.filter(seller_id=seller_session)
    return render(request,"seller/view_product.html",{"product":product_id})

def delete_product(request,id):
    x = Product.objects.get(id=id)
    x.delete()
    return redirect(view_product)

def edit_product(request,id):
    if request.method=='POST':
        try:
            na = request.POST['name']
            img = request.FILES['image']
            pr = request.POST['price']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Product.objects.get(id=id).Image
        Product.objects.filter(id=id).update(Title=na,Image=file,Price=pr)
        return redirect(view_product)
    else:
        pr = Product.objects.get(id=id)
        return render(request,"seller/edit_product.html",{"data":pr})
    
def order_details_(request):
    session = request.session['tid']
    user_id = User.objects.get(id=session)
    seller_session = Seller.objects.get(seller_id=user_id)
    product_id = Order.objects.filter(seller_id=seller_session.id).exclude(order_status="ORDER REJECTED")
    return render(request,"seller/order_details.html",{"product":product_id})

def confirm_order(request,id):
    order = Order.objects.filter(id=id).update(order_status="ORDER CONFIRMED")
    return redirect(order_details_)

def ready_order(request,id):
    order = Order.objects.filter(id=id).update(order_status="ORDER READY FOR DELIVERY")
    return redirect(order_details_)

def delivered_order(request,id):
    order = Order.objects.filter(id=id).update(order_status="ORDER DELIVERED")
    return redirect(order_details_)

def reject_order(request,id):
    order = Order.objects.filter(id=id).update(order_status="ORDER REJECTED")
    return redirect(order_details_)