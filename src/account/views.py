from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from pyexpat.errors import messages
from django.contrib import messages
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(generic.View):
   def get(self,request):
      form=RegisterForm()
      return render(request,'account/register.html',{'form':form})

   def post(self,request):
      form=RegisterForm(data=request.POST)
      if form.is_valid():
         login(request,form.save())
         return redirect('profile_create')

      return render(request,'account/register.html',{'form':form})

class LoginView(generic.View):

   def get(self,request):
      form=LoginForm()
      return render(request,'account/login.html',{'form':form})

   def post(self,request):
      form=LoginForm(data=request.POST)
      if form.is_valid():
         username=form.cleaned_data.get('username')
         password=form.cleaned_data.get('password')

         user=authenticate(username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect('home')

         messages.error(request,'username or password not valid ')

      return render(request,'account/login.html',{'form':form})


class LogoutView(LoginRequiredMixin,generic.View):
   def post(self,request):
      logout(request)
      return redirect('login')



