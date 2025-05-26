from django.urls import path
from . import views


urlpatterns=[
   path('',views.PostListView.as_view(),name='home'),
   path('post-create/',views.PostCreateView.as_view(),name='post_create'),
   path('post-detail/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
   path('post-update/<int:pk>/',views.PostUpdateView.as_view(),name='post_update'),
   path('post-delete/<int:pk>/',views.PostDeleteView.as_view(),name='post_delete'),

   # profile
   path('profile/',views.ProfileView.as_view(),name='profile'),
   path('profile-create',views.ProfileCreateView.as_view(),name='profile_create'),
   path('profile-update/',views.ProfileUpdateView.as_view(),name='profile_update'),
   path('delete-update/<int:pk>/',views.ProfileDeleteView.as_view(),name='profile_delete'),

   # like and comment

   path('like/<int:pk>',views.liking_post,name='post_like'),


]