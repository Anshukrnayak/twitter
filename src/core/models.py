from django.db import models
from django.contrib.auth.models import User


# Base model for common fields
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(BaseModel):
    """
        Profile : model for handle user profile :
    """
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    bio=models.CharField(max_length=250)
    profile_pic=models.ImageField(upload_to='profile',blank=True,null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Post model - Tweet or post
class Post(BaseModel):
    """
        Post model for handling user post
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=280)  # Twitter-style length
    post_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)  # No need for null or unique here

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"

# Comment model
class Comment(BaseModel):
    """
        Comment on user posts and assign new user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=280)

    def __str__(self):
        return f"{self.user.username} on {self.post.id}: {self.comment[:30]}"

# Follow model
class Follow(BaseModel):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_set')

    class Meta:
        unique_together = ('follower', 'following')  # Prevent duplicate follows

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
