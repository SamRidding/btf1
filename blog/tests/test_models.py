from django.test import TestCase, Client
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class TestBlogModel(TestCase):

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

    def test_post_model(self):
        self.client.login(
            username="testadmin", password="testpassword")

        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            image=SimpleUploadedFile(
                name='testimage.jpg',
                content=open('images/unittest/testimage.jpg', 'rb').read(),
                content_type='image/jpeg'),
            author=self.admin,
            status=1,
        )
        self.assertEqual(str(post), "Test Post")

    def test_comment_model(self):
        self.client.login(
            username="testuser", password="testpassword")

        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            image=SimpleUploadedFile(
                name='testimage.jpg',
                content=open('images/unittest/testimage.jpg', 'rb').read(),
                content_type='image/jpeg'),
            author=self.admin,
            status=1,
        )

        comment = Comment.objects.create(
            post=post,
            user=self.user,
            body="Test Comment",
        )
        self.assertEqual(str(comment.body),
                         "Test Comment")
