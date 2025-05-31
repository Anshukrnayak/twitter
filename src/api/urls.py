from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()

router.register(r'comment',views.CommentApiView,basename='comment')
router.register(r'post',views.CommentApiView,basename='post')
router.register(r'profile',views.ProfileApiView,basename='profile')


urlpatterns=[
   path('',include(router.urls))
]


