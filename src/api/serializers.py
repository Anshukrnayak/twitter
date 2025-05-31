from core.models import Post,Profile,Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
   class Meta:
      model=Comment
      fields=['post','comment']


class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
      model=Profile
      fields='__all__'

class PostSerializer(serializers.ModelSerializer):
   comments=CommentSerializer(read_only=True)
   class Meta:
      model=Post
      fields=['post_pic','content','likes','comments']

