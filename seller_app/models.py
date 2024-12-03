from django.db import models
from app.models import User


# Create your models here.

class Seller(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name
    
    
class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    Title = models.CharField(max_length=20)
    Image = models.ImageField(upload_to='uploads/')
    Price = models.IntegerField()

    def __str__(self):
        return self.Title