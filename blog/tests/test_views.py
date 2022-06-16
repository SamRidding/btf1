import tempfile
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment
from mixes.models import Mix


class TestBlogViews(TestCase):

    def setUp(self):

        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.admin = User.objects.create_superuser(
            username='testadmin',
            password='testpassword',
        )

        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.admin,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            status=1,
        )

        self.featuredpost = self.post

        self.mixes = Mix.objects.create(
            title="Test Post",
            slug="test-post",
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
        )

        self.home_page = (reverse('home'))
        self.blog = (reverse('blog'))

    def test_home_page_view(self):
        response = self.client.get(self.home_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_blog_view(self):
        response = self.client.get(self.blog)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog.html")
        self.assertTemplateUsed(response, "base.html")
    
