# Generated by Django 3.2.13 on 2022-06-05 14:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='save_release',
            field=models.ManyToManyField(blank=True, default=None, related_name='save_release', to=settings.AUTH_USER_MODEL),
        ),
    ]