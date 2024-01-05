from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Blog

class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.blog_data = {
            'title': 'Test Blog',
            'content': 'Lorem ipsum',
            'author': self.user,
        }

    def test_create_blog(self):
        blog = Blog.objects.create(**self.blog_data)
        self.assertEqual(blog.title, 'Test Blog')
        self.assertEqual(blog.content, 'Lorem ipsum')
        self.assertEqual(blog.author, self.user)

    def test_blog_str_representation(self):
        blog = Blog.objects.create(**self.blog_data)
        self.assertEqual(str(blog), 'Test Blog')
