from django.urls import path
from .views import Product_View,StoreView,CartView,Checkout
urlpatterns = [
    path('store/', StoreView.as_view(),name='store'),
    path('cart/', CartView.as_view(),name='cart'),
    path('checkout/', Checkout.as_view(),name='checkout'),
    path('detail/<int:pk>/', Product_View.as_view(), name='detail'),
]
