from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView

app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name = "list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name = "detail"),
    path("post/new/" , PostCreateView.as_view(), name = "post_create"),
    path("post/<slug:slug>/update/" , PostUpdateView.as_view(), name = "post_update"),
    path("post/<slug:slug>/delete/" , PostDeleteView.as_view(), name = "post_delete"),
]