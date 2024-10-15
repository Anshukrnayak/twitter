from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
   path('',views.Home_page.as_view(),name='home'),
   path('post/',views.Post_new_thread.as_view(),name='post'),


]
