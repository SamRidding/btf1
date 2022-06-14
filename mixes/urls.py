from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.Mixes.as_view(), name='mixes'),
    path('<slug:slug>/', views.MixPage.as_view(), name='mix_page'),
]
