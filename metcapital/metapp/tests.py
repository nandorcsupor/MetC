from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from metapp.models import Post

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_post(self):
        """
        Ensure we can create a new post.
        """
        url = reverse('post-list')
        data = {'title': 'Test Post', 'content': 'This is a test post.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_get_posts(self):
        """
        Ensure we can retrieve posts.
        """
        Post.objects.create(title='First Post', content='First Content')
        Post.objects.create(title='Second Post', content='Second Content')

        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        post = Post.objects.get(title='First Post')
        response = self.client.get(reverse('post-detail', kwargs={'pk': post.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'First Post')

    def test_update_post(self):
        """
        Ensure we can update a post.
        """
        post = Post.objects.create(title='Initial Title', content='Initial Content')
        response = self.client.put(reverse('post-detail', kwargs={'pk': post.id}), {'title': 'Updated Title', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Updated Title')

    def test_delete_post(self):
        """
        Ensure we can delete a post.
        """
        post = Post.objects.create(title='To be deleted', content='To be deleted')
        response = self.client.delete(reverse('post-detail', kwargs={'pk': post.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(pk=post.id).exists())
