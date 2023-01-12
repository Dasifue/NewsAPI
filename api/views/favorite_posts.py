from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from ..models import FavoritePost, Post
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
        data = {}
        k = 1
        for ser_data in serializer.data:
            ser_data = dict(ser_data)
            post_id = ser_data.get("post")
            ser_data["post"] = self.get_post_data(pk=post_id)
            data.update({k:ser_data})
            k+=1
        return Response(data=data, status=status.HTTP_200_OK)


class FavoritePostCreateAPIView(CreateAPIView):
    model = FavoritePost
    serializer_class = FavoritePostCreateSerializer
    permission_classes = (IsAuthenticated, )


class FavoritePostsDeleteAPIView(DestroyAPIView):
    model = FavoritePost
    serializer_class = FavoritePostsDeleteSerializer
    queryset = FavoritePost.objects.all()
    lookup_field = "pk"
    permission_classes = (ISAuthor,)