from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    user_type = models.CharField(max_length=20,blank=False,verbose_name="user_type")
    approve_seller = models.CharField(max_length=20,blank=False,verbose_name="approve_seller")

    def __str__(self):
        return self.first_name