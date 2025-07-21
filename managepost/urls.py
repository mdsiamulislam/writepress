from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create_post_home/', views.create_post_home, name='create'),
    path('create_post/', views.create_post, name='create_post'),
]
