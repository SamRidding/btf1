from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("", views.UserProfile.as_view(), name="userprofile"),
    path('add/<int:id>/', views.add_release, name='add_release'),
    path("", views.saved_releases, name='userprofile'),
]