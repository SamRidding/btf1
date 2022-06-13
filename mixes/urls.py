from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.MixPage().as_view(), name='mix_page'),
]
