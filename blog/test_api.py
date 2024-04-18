from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.utils.timezone import make_aware
from datetime import datetime
from blog.models import Post

class PostAPITests(APITestCase):
    def setUp(self):
        # Создаем пользователя и его токен для аутентификации
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

        # Создаем пример поста
        self.post = Post.objects.create(
            title="Test Post",
            content="Test content",
            published_date=make_aware(datetime(2021, 1, 1))
        )

    def test_get_posts(self):
        # Тест получения списка постов
        response = self.client.get(reverse('blog:post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_post_authenticated(self):
        # Тест на создания поста аутентифицированным юзером
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {"title": "Nice post", "content": "Very nice content"}
        response = self.client.post(reverse('blog:post-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_post_unauthenticated(self):
        # Попытка создания поста аутентифицированным юзером
        data = {"title": "Nice post", "content": "Very nice content"}
        response = self.client.post(reverse('blog:post-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_post_authenticated(self):
        # Тест на удаление поста аутентифицированным юзером
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(reverse('blog:post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_post_unauthenticated(self):
        # Попытка удаления неаутентифицированным юзером
        response = self.client.delete(reverse('blog:post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class CommentAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.post = Post.objects.create(title="Test Post", content="Test Content")

    def test_add_comment_authenticated(self):
        # Тест на комментирование аутентифицированным юзером
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {"comment_text": "Nice post", "author_name": "Test User"}
        url = reverse('blog:add_comment_to_post', kwargs={'pk': self.post.pk})
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # Юзер авторизован, поэтому должно разрешить

    def test_add_comment_unauthenticated(self):
        # Попытка комментирования неаутентифицированным юзером
        data = {"comment_text": "Nice post", "author_name": "Test User"}
        url = reverse('blog:add_comment_to_post', kwargs={'pk': self.post.pk})
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) # Должно требовать авторизацию