from rest_framework.serializers import ModelSerializer

from ..models import Post


class PostsListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "slug",
            "author",
            "title",
            "short_description",
            "image",
            "created_at"
        )


class PostDetailsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"



class UsersPostsListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "slug",
            "title",
            "short_description",
            "image",
            "created_at",
            )

class UserPostRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "slug",
            "title",
            "short_description",
            "description",
            "image",
            "created_at"
        )