from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",view=views.index, name="home"),
    path("post/<int:pk>", view=views.PostDetailView.as_view(), name="post-details")
]