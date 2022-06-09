from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("blog/", views.Blog.as_view(), name="blog"),
    path('add_post/', views.AddPost, name='add_post'),
    path('delete_comment/<int:comment_id>/', views.DeleteComment,
         name="delete_comment"),
    path('edit_post/<slug:slug>/', views.EditPost, name='edit_post'),
    path('delete_post/<slug:slug>/', views.DeletePost, name="delete_post"),
    path('<slug:slug>/', views.BlogPost.as_view(), name='blog_post'),
]
