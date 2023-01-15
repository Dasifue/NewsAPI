from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from ..models import FavoritePost, Post
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ..permissions import ISAuthor

from ..models import Comment

from ..serializers.comments_serializer import (
    CommentsCreateSerializer,
    CommentUpdateDestroySerializer,
    CommentToCommentCreateSerializer
)

class CommentCreateAPIView(CreateAPIView):
    model = Comment
    serializer_class = CommentsCreateSerializer
    permission_classes = (IsAuthenticated,)


class CommentUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateDestroySerializer
    lookup_field = "pk"
    permission_classes = (ISAuthor,)


class CommentToCommentCreateAPIView(CreateAPIView):
    model = Comment
    serializer_class = CommentToCommentCreateSerializer
    permission_classes = (IsAuthenticated,)