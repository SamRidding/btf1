import tempfile
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from blog.models import Post

class TestUserProfileViews(TestCase):

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

        self.userprofile = (reverse('userprofile'))

    def test_user_profile_view(self):
        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.userprofile)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "userprofile/userprofile.html")
        self.assertTemplateUsed(response, "base.html")

