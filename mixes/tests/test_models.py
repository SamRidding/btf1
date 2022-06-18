from django.test import TestCase, Client
from mixes.models import Mix
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class TestMixModel(TestCase):

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

    def test_mix_model(self):
        self.client.login(
            username="testadmin", password="testpassword")

        post = Mix.objects.create(
            title="Test Mix",
            slug="test-mix",
            image=SimpleUploadedFile(
                name='testimage.jpg',
                content=open('images/unittest/testimage.jpg', 'rb').read(),
                content_type='image/jpeg'),
        )
        self.assertEqual(str(post), "Test Mix")