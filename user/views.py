from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.contrib import messages
from store.models import Customer
from django.contrib.auth.models import User

class SignUp(View):

    def get(self,request):

        form=SignUpForm()
        return render(request,'user/signup.html',{'form':form})

    def post(self,request):
        form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            name=request.POST.get('first_name')+'  '+request.POST.get('last_name')
            email=request.POST.get('email')
            user=User.objects.get(email=email)
            customer=Customer(name=name,email=email,user=user)
            customer.save()
            messages.success(request, 'Your account has been created. Now login..')
        return redirect('store')
