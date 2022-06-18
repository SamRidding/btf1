from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import home_page, Blog, search_blog, add_post, BlogPost, \
     delete_comment, edit_post, delete_post


class TestBlogUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home_page)

    def test_blog_url_is_resolved(self):
        url = reverse('blog')
        self.assertEquals(resolve(url).func.view_class, Blog)

    def test_search_blog_url_is_resolved(self):
        url = reverse('search_blog')
        self.assertEquals(resolve(url).func, search_blog)

    def test_add_post_url_is_resolved(self):
        url = reverse('add_post')
        self.assertEquals(resolve(url).func, add_post)

    def test_delete_comment_url_is_resolved(self):
        url = reverse('delete_comment', args=[1])
        self.assertEquals(resolve(url).func, delete_comment)

    def test_edit_post_url_is_resolved(self):
        url = reverse('edit_post', args=['test-slug'])
        self.assertEquals(resolve(url).func, edit_post)

    def test_delete_post_url_is_resolved(self):
        url = reverse('delete_post', args=['test-slug'])
        self.assertEquals(resolve(url).func, delete_post)

    def test_blogpost_url_is_resolved(self):
        url = reverse('blog_post', args=['test-slug'])
        self.assertEquals(resolve(url).func.view_class, BlogPost)