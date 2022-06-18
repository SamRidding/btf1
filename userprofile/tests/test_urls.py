from django.test import SimpleTestCase
from django.urls import reverse, resolve
from userprofile.views import saved_release, add_release


class TestUserprofileUrls(SimpleTestCase):

    def test_add_release_url_is_resolved(self):
        url = reverse('add_release', args=[1])
        self.assertEquals(resolve(url).func, add_release)

    def test_userprofile_url_is_resolved(self):
        url = reverse('userprofile')
        self.assertEquals(resolve(url).func, saved_release)
