from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from blog.forms import CommentForm, AddPostForm, EditPostForm


class TestBlogForms(TestCase):

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

    def test_comment_form(self):
        self.client.login(
            username="testuser", password="testpassword")

        form = CommentForm({
            "body": "Test comment",
        })
        self.assertTrue(form.is_valid())

    '''
    The following two tests fail and I have covered this in the unit testing
    section of the testing markdown file
    '''

    def test_add_post_form(self):
        self.client.login(
            username="testadmin", password="testpassword")

        form = AddPostForm(data={
            "title": "Test Post",
            "image": SimpleUploadedFile(
                name='testimage.jpg',
                content=open('images/unittest/testimage.jpg', 'rb').read(),
                content_type='image/jpeg'),
            "music_preview": "https://www.youtube.com/watch?v=2a0plULkAPA",
            "content": "Test Post",
            "status": 1,
        })
        print(form.data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_edit_post_form(self):
        self.client.login(
            username="testadmin", password="testpassword")

        form = EditPostForm({
            "title": "Test Post",
            "image": SimpleUploadedFile(
                name='testimage.jpg',
                content=open('images/unittest/testimage.jpg', 'rb').read(),
                content_type='image/jpeg'),
            "music_preview": "https://www.youtube.com/watch?v=2a0plULkAPA",
            "content": "Test Post",
            "status": 1,
        })
        self.assertTrue(form.is_valid())
