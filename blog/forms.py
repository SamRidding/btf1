from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'image', 'content',
                  'music_preview', 'status')


class EditPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'image', 'content', 
                  'slug', 'music_preview', 'status')
