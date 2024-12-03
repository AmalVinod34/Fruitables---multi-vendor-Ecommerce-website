from django.db import models
from app.models import User
from seller_app.models import Product,Seller

# Create your models here.

class Customer(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

    def __str__(self):
        return self.Name
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    seller = models.ForeignKey(Product,on_delete=models.CASCADE)
    Title = models.CharField(max_length=20)
    Image = models.ImageField(upload_to='uploads')
    Quantity = models.IntegerField(default=1)
    Price = models.IntegerField()
    def __str__(self):
        return self.Title
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to='uploads')
    product_quantity = models.IntegerField(default=1)
    Name = models.CharField(max_length=10,null=True)
    Email = models.EmailField(null=True)
    Address = models.CharField(max_length=60,null=True)
    Phone = models.IntegerField(null=True)
    Total = models.IntegerField(null=True)
    order_status = models.CharField(max_length=20,verbose_name="order_status")

    def __str__(self):
        return self.Name