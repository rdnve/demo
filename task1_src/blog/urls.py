from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.root, name="root"),
    path("about/", views.about, name="about"),
    path("technology/", views.technology, name="technology"),
    path("feedback/", views.feedback, name="feedback"),
    path("category/<str:name>/", views.category, name="category"),
    path("post/<str:slug>/", views.post_detail, name="post_detail"),
    path("year/", views.year, name="year"),
]
