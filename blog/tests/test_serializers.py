from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Blog
from blog.serializers import UserSerializer, BlogSerializer

User = get_user_model()

class UserSerializerTest(TestCase):
    def setUp(self):
        self.validated_data = {'username': 'testuser', 'password': 'testpassword'}
        self.invalidated_data = {'username': 'testuser', 'password': ''}

    def test_create_user_valid_data(self):
        serializer = UserSerializer(data=self.validated_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, User)

    def test_create_user_invalid_data(self):
        serializer = UserSerializer(data=self.invalidated_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)

class BlogSerializerTest(TestCase):
    def setUp(self):
        self.validated_data = {'title': 'Test Blog', 'content': 'Lorem ipsum', 'author': User.objects.create(username='testuser')}
        self.invalidated_data = {'title': '', 'content': 'Lorem ipsum', 'author': User.objects.create(username='testuser')}

    def test_create_blog_valid_data(self):
        serializer = BlogSerializer(data=self.validated_data)
        self.assertTrue(serializer.is_valid())
        blog = serializer.save()
        self.assertIsInstance(blog, Blog)

    def test_create_blog_invalid_data(self):
        serializer = BlogSerializer(data=self.invalidated_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)
