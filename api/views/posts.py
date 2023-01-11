from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Post
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ..permissions import ISAuthor

from ..serializers.posts_serializer import (
    PostsListSerializer,
    PostDetailsSerializer,
    UsersPostsListSerializer,
    UserPostRetrieveUpdateDestroySerializer
)


class PostsListAPIView(ListAPIView):
    model = Post
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostsListSerializer


class PostDetailsAPIView(RetrieveAPIView):
    model = Post
    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostDetailsSerializer


class UsersPostsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        return user

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        posts = Post.objects.filter(author=self.object).order_by("-created_at")
        serializer = UsersPostsListSerializer(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserPostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = UserPostRetrieveUpdateDestroySerializer
    queryset = Post.objects.all()
    lookup_field = "slug"
    permission_classes = (ISAuthor,)
