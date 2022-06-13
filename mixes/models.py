from django.db import models
from embed_video.fields import EmbedVideoField

class Mix(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    posted_on = models.DateField(auto_now_add=True)
    image = models.ImageField()
    content = models.TextField(blank=True)
    music_preview = EmbedVideoField(blank=True)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return str(self.title)
