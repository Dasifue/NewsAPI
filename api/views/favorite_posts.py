from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from ..models import FavoritePost, Post

from users.models import MainUser

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ..permissions import ISAuthor

from ..serializers.posts_serializer import (
    PostDetailsSerializer
)

from ..serializers.favorite_posts_serializer import (
    FavoritePostsListSerializer,
    FavoritePostsDeleteSerializer,
    FavoritePostCreateSerializer
)

class FavoritePostsListAPIView(ListAPIView):
    model = FavoritePost
    serializer_class = FavoritePostsListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = FavoritePost.objects.filter(Mainuser=self.request.user)
        return queryset

    def get_post_data(self, pk):
        obj = Post.objects.get(pk=pk)
        serializer = PostDetailsSerializer(instance=obj)
        return serializer.data
        


    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(instance=queryset, many=True)
        data = []
        for ser_data in serializer.data:
            ser_data = dict(ser_data)
            post_id = ser_data.get("post")
            ser_data["post"] = self.get_post_data(pk=post_id)
            data.append(ser_data)
        return Response(data=data, status=status.HTTP_200_OK)


class FavoritePostCreateAPIView(CreateAPIView):
    model = FavoritePost
    serializer_class = FavoritePostCreateSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        post = Post.objects.get(id=request.data.get("post"))
        user = MainUser.objects.get(username=request.user)
        favorites = FavoritePost.objects.filter(Mainuser=user, post=post)
        if not favorites:
            favorite = FavoritePost.objects.create(Mainuser=user, post=post)
            favorite.save()
            return Response(data={"success": "added"}, status=status.HTTP_201_CREATED)
        return Response(data={"Error": "already in favorites"})
        


class FavoritePostsDeleteAPIView(DestroyAPIView):
    model = FavoritePost
    serializer_class = FavoritePostsDeleteSerializer
    queryset = FavoritePost.objects.all()
    lookup_field = "pk"
    permission_classes = (ISAuthor,)