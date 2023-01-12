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

from .views.favorite_posts import (
    FavoritePostsListAPIView,
    FavoritePostCreateAPIView,
    FavoritePostsDeleteAPIView
)

from .views.comments import (
    CommentCreateAPIView,
    CommentUpdateDestroyAPIView
)

app_name = "api"

urlpatterns = [
    path("categories/list/", CategoriesListAPIView.as_view(), name="categories"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category_create"),
    path("categories/details/<str:slug>", CategoryDetailsUpdateDestroyAPIView.as_view(), name="category_details"),

    path("posts/list/", PostsListAPIView.as_view(), name="posts"),
    path("posts/details/<str:slug>", PostDetailsAPIView.as_view(), name="post_details"),
    path("posts/user/", UsersPostsAPIView.as_view(), name="users_posts"),
    path("posts/update/<str:slug>", UserPostRetrieveUpdateDestroyAPIView.as_view(), name="post_update"),

    path("user/favorite/list/", FavoritePostsListAPIView.as_view(), name="favorite_posts"),
    path("user/favorite/create/", FavoritePostCreateAPIView.as_view(), name="favorite_post_create"),
    path("user/favorite/delete/<int:pk>", FavoritePostsDeleteAPIView.as_view(), name="delete_favorite_post"),

    path("posts/comment/create/", CommentCreateAPIView.as_view(), name="comment_create"),
    path("posts/comment/update/<int:pk>", CommentUpdateDestroyAPIView.as_view(), name="comment_update")
]