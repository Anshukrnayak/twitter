from rest_framework import serializers
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

class RegisterSerializer(serializers.ModelSerializer):
   password1=serializers.CharField(write_only=True)
   password2=serializers.CharField(write_only=True)
   class Meta:
      model=User
      fields=['username','email','password1','password2']

   def validate(self, attrs):
      password1=attrs['password1']
      password2=attrs['password2']

      if len(password1)<8:
         raise serializers.ValidationError('Password should be at least 8 characters long.')

      if password1!=password2:
         raise serializers.ValidationError('Passwords not matched ')

      return attrs

   def create(self, validated_data):
      password=validated_data('password1').pop()
      validated_data('password2').pop()


      user=User.objects.create_user(password=password,**validated_data)

      return user


class LoginSerializer(serializers.Serializer):
   username=serializers.CharField(write_only=True)
   password=serializers.CharField(write_only=True)


   def validate(self, attrs):
      password=attrs.get('password')
      username=attrs.get('username')

      user=authenticate(username=username,password=password)
      if user is None:
         raise serializers.ValidationError('Invalid username or password')

      if not user.is_active:
         raise serializers.ValidationError('User is disabled ')

      attrs['user']=user
      return attrs

