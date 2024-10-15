from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('signup/',views.SignupPage.as_view(),name='signup'),
    path('login/',views.LoginPage.as_view(),name='login'),
    path('logout/',views.LogoutPage,name='logout'),


]
