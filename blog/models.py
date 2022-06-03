from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    music_preview = EmbedVideoField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["posted_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"
