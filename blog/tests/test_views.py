from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from blog.models import Blog

User = get_user_model()


class UserRegistrationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/register/"
        self.valid_data = {"username": "testuser", "password": "testpassword"}
        self.invalid_data = {"username": "testuser", "password": ""}

    def test_user_registration_valid_data(self):
        response = self.client.post(self.url, self.valid_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)

    def test_user_registration_invalid_data(self):
        response = self.client.post(self.url, self.invalid_data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.count(), 0)


class BlogListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/blogs/"
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.valid_data = {"title": "Test Blog", "content": "Lorem ipsum","author": self.user.id}
        self.invalid_data = {"title": "", "content": "Lorem ipsum"}

    def test_blog_list_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_blog_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url,  self.valid_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Blog.objects.count(), 1)

    def test_create_blog_unauthenticated_user(self):
        response = self.client.post(self.url, self.valid_data, format="json")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(Blog.objects.count(), 0)


class BlogRetrieveUpdateDeleteViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.blog = Blog.objects.create(
            title="Test Blog", content="Lorem ipsum", author=self.user
        )
        self.url = f"/api/blogs/{self.blog.id}/"
        self.valid_data = {"title": "Updated Blog Title", "content": "Updated content"}

    def test_retrieve_blog_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_blog_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.url, self.valid_data, format="json")
        self.assertEqual(response.status_code, 400)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, "Test Blog")

    def test_delete_blog_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Blog.objects.count(), 0)

    def test_delete_blog_unauthenticated_user(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(Blog.objects.count(), 1)
