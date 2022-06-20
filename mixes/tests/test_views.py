import tempfile
from django.test import TestCase, Client
from django.urls import reverse
from mixes.models import Mix


class TestMixesViews(TestCase):

    def setUp(self):

        self.client = Client()

        self.mix = Mix.objects.create(
            title="Test Post",
            slug="test-post",
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
        )

        self.mixpage = (reverse('mix_page',
                                kwargs={"slug": self.mix.slug}))
        self.mixes = (reverse('mixes'))

    def test_mix_page_view(self):
        response = self.client.get(self.mixpage)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mixes/mix_page.html")
        self.assertTemplateUsed(response, "base.html")

    def test_mixes_view(self):
        response = self.client.get(self.mixes)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mixes/all.html")
        self.assertTemplateUsed(response, "base.html")
