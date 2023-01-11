from django.urls import path

from .views.categories import (
    CategoriesListAPIView,
    CategoryCreateAPIView,
    CategoryDetailsUpdateDestroyAPIView
    )

from .views.posts import (
    PostsListAPIView,
    PostDetailsAPIView,
    UsersPostsAPIView,
    UserPostRetrieveUpdateDestroyAPIView
)

app_name = "api"

urlpatterns = [
    path("categories/list/", CategoriesListAPIView.as_view(), name="categories"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category_create"),
    path("categories/details/<str:slug>", CategoryDetailsUpdateDestroyAPIView.as_view(), name="category_details"),

    path("posts/list/", PostsListAPIView.as_view(), name="posts"),
    path("posts/details/<str:slug>", PostDetailsAPIView.as_view(), name="post_details"),
    path("posts/user/", UsersPostsAPIView.as_view(), name="users_posts"),
    path("posts/update/<str:slug>", UserPostRetrieveUpdateDestroyAPIView.as_view(), name="post_update")
]