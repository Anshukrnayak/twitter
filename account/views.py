from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignupForm
from django.contrib.auth.decorators import login_required


class SignupPage(View):


    def get(self,request): 
        form=SignupForm()

        return render(request,'account/signup.html',{'form':form})


    def post(self,request):


        form=SignupForm(request.POST)

        if form.is_valid():
            login(request,form.save())

            return redirect('home')
        

        return render(request,'account/signup.html',{'form':form})

        
class LoginPage(View):

    def get(self,request):
        
        form=AuthenticationForm()

        return render(request,'account/login.html',{'form':form}) 
    
    def post(self,request):

        form=AuthenticationForm(data=request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(username=username,password=password)


            if user is not None:
                login(request,user)

                return redirect('home')

        return render(request,'account/login.html',{'form':form})



@login_required
def LogoutPage(request):

    logout(request)

    return redirect('home')
