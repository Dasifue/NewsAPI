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
            "image"
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
            "image"
            )

class UserPostRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "short_description",
            "description",
            "image"
        )