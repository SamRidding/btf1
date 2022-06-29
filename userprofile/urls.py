from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add/<int:id>/', views.add_release, name='add_release'),
    path("", views.saved_release, name='userprofile'),
]
