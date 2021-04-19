from django.db import models
from  django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price=models.FloatField()
    digital=models.BooleanField(default=False)
    #image=
    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_added=models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False,blank=False,null=True)
    transaction_id=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)

class CartItems(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True) #
    order=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateField(auto_now_add=True)

