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
    image=models.ImageField(blank=True,upload_to='images',default='images/placeholder.png')

    def __str__(self):
        return self.name
    @property
    def image_url(self):
        try:
            url=self.image.url
        except:
            url='https://image.freepik.com/free-psd/book-cover-mockup_125540-453.jpg'
        return url

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_added=models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False,blank=False,null=True)
    transaction_id=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True) #
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateField(auto_now_add=True)
    @property
    def total_price(self):
        t=self.quantity*self.product.price
        return t

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    address=models.CharField(max_length=200, null=True)
    city=models.CharField(max_length=200, null=True)
    state=models.CharField(max_length=200, null=True)
    zipcode=models.CharField(max_length=200, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address


