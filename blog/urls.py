from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("blog/", views.Blog.as_view(), name="blog"),
    path("search/", views.search_blog, name="search_blog"),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment,
         name="delete_comment"),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete_post/<slug:slug>/', views.delete_post, name="delete_post"),
    path('<slug:slug>/', views.BlogPost.as_view(), name='blog_post'),
]
