from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",view=views.index, name="home"),
    path("<int:pk>", view=views.PostDetailView.as_view(), name="post-details"),
    path('categori', view=views.CatergoriList.as_view(), name="categori_list"),
     path('author', view=views.AuthorList.as_view(), name="author_list"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)