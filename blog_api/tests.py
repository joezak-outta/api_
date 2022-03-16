from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category
from django.contrib.auth.models import User
# Create your tests here.


class PostTests(APITestCase):
    def test_view_post(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.test_user1 = User.objects.create_user(
            username='john', password='doe1234@')
        data = {"title": "new post", "author": 3,
                "excerpt": "new post", "content": "new django post"}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def update_post(self):
        client = APIClient()
        self.test_category = Category.objects.create(name="Python")
        self.testUser1 = User.objects.create_user(
            username='test_user1', password='12345678')
        self.testUser2 = User.objects.create_user(
            username='test_user2', password='1234567')
        test_post = Post.objects.create(category_id)
