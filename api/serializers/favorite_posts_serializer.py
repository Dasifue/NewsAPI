from rest_framework.serializers import ModelSerializer

from ..models import FavoritePost
from users.models import MainUser

class FavoritePostsListSerializer(ModelSerializer):
    class Meta:
        model = FavoritePost
        fields = (
            "id",
            "post",
            "created_at"
        )


class FavoritePostCreateSerializer(ModelSerializer):
    class Meta:
        model = FavoritePost
        fields = (
            "post",
        )

    def create(self, validated_data):
        user = self.context['request'].user
        user = MainUser.objects.get(username=user)
        post = validated_data.get("post")
        favorite_post = FavoritePost.objects.create(
            Mainuser=user,
            post=post
        )
        favorite_post.save()
        return favorite_post


class FavoritePostsDeleteSerializer(ModelSerializer):
    class Meta:
        model = FavoritePost
        fields = "__all__"