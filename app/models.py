from django.db import models
from django.contrib.auth.models import User




class follow(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    follows=models.ManyToManyField(User,blank=True,related_name='follow')


class PostThread(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/' , blank=True)
    text_content=models.TextField(null=True,blank=True)
    like_count=models.IntegerField(default=0,null=True)

    def __str__(self): return self.name


