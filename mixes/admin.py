from django.contrib import admin
from .models import Mix


@admin.register(Mix)
class MixAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'posted_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}