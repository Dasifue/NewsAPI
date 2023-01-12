from rest_framework.serializers import ModelSerializer

from ..models import Post

from users.models import MainUser

import random

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


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "short_description",
            "description",
            "category",
            "image"
        )

    def create_slug(self):
        name = self.validated_data.get("title").lower()
        name = name.replace(" ", "")[::random.randint(2,4)]
        coding = coding = random.randrange(1000, 99999, 1)
        slug = f"{name}{coding}"
        return slug

    def create(self, validated_data):
        user = self.context['request'].user
        user = MainUser.objects.get(username=user)
        title = validated_data.get("title")
        short_description = validated_data.get("short_description")
        description = validated_data.get("description")
        category = validated_data.get("category")
        image = validated_data.get("image")
        slug = self.create_slug()
        post = Post.objects.create(
            author=user,
            title=title,
            short_description=short_description,
            description=description,
            category=category,
            image=image,
            slug=slug
        )
        post.save()
        return post