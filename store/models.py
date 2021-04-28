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
    description=models.TextField(blank=True,null=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,default=1)

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
    @property
    def cart_total_price(self):
        order_items=self.cartitem_set.all()
        total=sum([item.total_price for item in order_items])
        # total=0
        # for item in order_items:
        #     total += item.total_price
        return total
    @property
    def total_items(self):
        order_items=self.cartitem_set.all()
        total = sum([item.quantity for item in order_items])
        # total=0
        # for item in order_items:
        #     total += item.quantity
        return total

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True) #
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateField(auto_now_add=True)
    @property
    def total_price(self):
        total=self.quantity*self.product.price
        return total
    def __str__(self):
        return str(self.product.name)

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

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
