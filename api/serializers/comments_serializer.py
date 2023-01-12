from rest_framework.serializers import ModelSerializer

from ..models import Comment

from users.models import MainUser

class CommentsListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "text",
            "created_at"
        )


class CommentsCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "post",
            "text"
        )

    def create(self, validated_data):
        user = self.context['request'].user
        user = MainUser.objects.get(username=user)
        text = validated_data.get("text")
        post = validated_data.get("post")
        comment = Comment.objects.create(
            author=user,
            text=text,
            post = post
        )
        comment.save()
        return comment


class CommentUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "text", 
        )