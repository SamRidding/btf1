from . import views
from django.urls import path

urlpatterns = [
    path("", views.UserProfile.as_view(), name="userprofile"),
]