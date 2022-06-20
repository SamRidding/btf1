from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mixes.views import Mixes, MixPage


class TestMixesUrls(SimpleTestCase):

    def test_mixes_url_is_resolved(self):
        url = reverse('mixes')
        self.assertEquals(resolve(url).func.view_class, Mixes)

    def test_mix_page_url_is_resolved(self):
        url = reverse('mix_page', args=['test-slug'])
        self.assertEquals(resolve(url).func.view_class, MixPage)
