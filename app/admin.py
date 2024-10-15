from django.contrib import admin
from .models import PostThread,follow

@admin.register(PostThread)
class PostAdmin(admin.ModelAdmin):
    list_display=['user','image','text_content','like_count']



@admin.register(follow)
class FollowAdmin(admin.ModelAdmin):
    list_display=['user']
