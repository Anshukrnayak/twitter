from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment, Follow

class TestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Abhijeet', password='#include')

        # First, create and save the post
        self.post = Post.objects.create(user=self.user, content='First content')

        # Then add a like after saving the post
        self.post.likes.add(self.user)

        # Now you can create a comment with the post
        self.comment = Comment.objects.create(
            user=self.user,
            post=self.post,
            comment='first comment'
        )

    def test_comment_linked_to_post(self):
        self.assertEqual(self.comment.post, self.post)

    def test_comment_user(self):
        self.assertEqual(self.comment.user.username, 'Abhijeet')

    def test_post_likes(self):
        self.assertIn(self.user, self.post.likes.all())
