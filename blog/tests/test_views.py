import tempfile
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
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
        self.search_blog = (reverse('search_blog'))
        self.blogpost = (reverse('blog_post',
                                 kwargs={"slug": self.post.slug}))

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

    def test_search_blog_view(self):
        response = self.client.get(self.search_blog)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/search_blog.html")
        self.assertTemplateUsed(response, "base.html")

    def test_blog_post_view(self):
        response = self.client.get(self.blogpost)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_post.html")
        self.assertTemplateUsed(response, "base.html")


class TestUpdateBlogViews(TestCase):
    
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
            image=SimpleUploadedFile(
                name='testimage.jpg',
                content=open('images/unittest/testimage.jpg', 'rb').read(),
                content_type='image/jpeg'),
            status=1,
        )

        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            body="Test comment",
        )

        self.add_post = (reverse('add_post'))
        self.blog = (reverse('blog'))

    def test_admin_add_blog_post(self):
        self.client.login(
            username="testadmin", password="testpassword")
        response = self.client.get(self.add_post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_post.html")
        self.assertTemplateUsed(response, "base.html")

    def test_user_add_blog_post(self):
        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.add_post)
        self.assertRedirects(response, self.blog)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'You do not have permission to add blog posts')

    def test_admin_add_invalid_post(self):

        self.client.login(
            username="testadmin", password="testpassword")
        response = self.client.post(self.add_post, {
            "title": 1,
            "slug": 1,
            "author": 1,
            "image": 1,
            "status": 1,
        })

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "The post could not be submitted. \
                                Please try again.")
        self.assertRedirects(response, self.add_post)

    def test_admin_add_valid_post(self):

        self.client.login(
            username="testadmin", password="testpassword")
        response = self.client.post(self.add_post, {
            "title": "Test Post 2",
            "slug": "test-post-2",
            "image": SimpleUploadedFile(
                name='testimage.jpg',
                content=open('images/unittest/testimage.jpg', 'rb').read(),
                content_type='image/jpeg'),
            "author": self.admin,
            "status": 1,
        })

        post = Post.objects.get(title="Test Post 2")

        self.assertEqual(post.title, "Test Post 2")
        self.assertEqual(post.slug, "test-post-2")
        self.assertEqual(post.author, self.admin)
        self.assertEqual(post.status, 1)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "The post has been added to the blog.")
        self.assertRedirects(response, reverse(
            'blog_post', kwargs={"slug": post.slug}))