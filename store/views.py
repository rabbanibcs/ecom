from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    products=Product.objects.all()
    context={'products' : products }
    return render(request,'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order=Order.objects.get(customer=customer)
        items=order.cartitem_set.all()
    else:
        items=[]

    # total_price=float(items.quantity)*float(items.price)
    context={'items':items}
    return render(request,'store/cart.html',context)
    
def checkout(request):
    context={}
    return render(request,'store/checkout.html',context)
    