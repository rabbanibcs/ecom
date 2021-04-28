from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('signout/', LogoutView.as_view(template_name='user/signout.html'), name='signout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('signin/', LoginView.as_view(template_name='user/signin.html'), name='signin'),
]