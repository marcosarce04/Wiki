from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("savenewpage", views.savenewpage, name="savenewpage"),
    path("edit", views.edit, name="edit"),
    path("savedition", views.savedition, name="savedition"),
    path("random", views.random, name="random")
]
