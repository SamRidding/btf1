from django.contrib import admin
from . models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'status', 'posted_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'posted_on')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'posted_on')
