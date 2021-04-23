from django.shortcuts import render, reverse, redirect
from django.views import View
from .models import Customer,Product,Order,CartItem,ShippingAddress


class StoreView(View):

    def get(self,request):
        products=Product.objects.all()
        context={'products' : products }
        return render(request,'store/store.html',context)

class CartView(View):

    def get(self,request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer)
            items = order.cartitem_set.all()
            context = {'items': items, 'order': order}
        else:
            items = []
            context = {'items': items,}
        return render(request, 'store/cart.html', context)

class Checkout(View):

    def get(self,request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order = Order.objects.get(customer=customer)
            items = order.cartitem_set.all()
            context = {'items': items, 'order': order}
        else:
            items = []
            context = {'items': items, }
        return render(request, 'store/checkout.html', context)

class Product_View(View):

    def get(self,request,**kwargs):
        product=Product.objects.get(pk=kwargs['pk'])
        context={'product' : product }
        return render(request,'store/detail.html',context)

    def post(self,request,pk):
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        product = Product.objects.get(pk=pk)
        item, created = CartItem.objects.get_or_create(order=order, product=product)
        item.quantity += 1
        item.save()
        return redirect('store')






# def checkout(request):
#
#     if request.user.is_authenticated:
#         customer=request.user.customer
#         order=Order.objects.get(customer=customer)
#         items=order.cartitem_set.all()
#         context = {'items': items, 'order': order}
#     else:
#         items=[]
#         context = {'items': items,}
#     return render(request,'store/checkout.html',context)


# def cart(request):
#     if request.user.is_authenticated:
#         customer=request.user.customer
#         order,created=Order.objects.get_or_create(customer=customer)
#         items=order.cartitem_set.all()
#         context = {'items': items, 'order': order}
#     else:
#         items=[]
#         context = {'items': items,}
#     return render(request,'store/cart.html',context)


# def store(request):
#     if request.method=='GET':
#         products=Product.objects.all()
#         context={'products' : products }
#         return render(request,'store/store.html',context)

# products=Product.objects.all()
# context={'products' : products }
# return render(request,'store/store.html',context)

# class Product_View(View):
#     def get(self,request,pk):
#         product=Product.objects.get(pk=pk)
#         context={'product' : product }
#         return render(request,'store/detail.html',context)
# class ProductView(DetailView):
#
#     model = Product
#     template_name = 'store/detail.html'

# class UpdateCart(UpdateView):
#     customer = request.user.customer
#     product = Product.objects.ge(pk=product_id)
#     model = CartItem
#     fields = ['quantity','']

    # if request.method=='POST':
    #     form=CartForm(request.POST)
        # return redirect('store')

# def add_to_cart(request,pk):
#     customer = request.user.customer
#     product=Product.objects.get(pk=pk)
#     order, created = Order.objects.get_or_create(customer=customer,complete=False)
#     item,created= CartItem.objects.get_or_create(order=order,product=product)
#     item.quantity+=1
#     item.save()
#     return render(reverse('store'))
