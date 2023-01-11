from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import MainUser
from api.models import Post

from .serializers import (
    UserCreateSerializer,
    UsersListSerializer,
    UserDetailsSerializer,
    UserUpdateSerializer,
    UserPasswordUpdateSerializer
)

from rest_framework.permissions import IsAuthenticated 

from api.serializers.posts_serializer import UsersPostsListSerializer

class UserCreateAPIView(CreateAPIView):
    model = MainUser
    serializer_class = UserCreateSerializer

    def get(self, request):
        data = {
            "information": "create MainUser with fields",
            "fields": {
                "first_name": "char field, max_length 150, not required",
                "last_name": "char field, max_length 150, not required",
                "username": "char field, max_length 150, unique, required",
                "email": "email field, not required",
                "password1": "char field, max_length 128, required",
                "password2": "char field, max_length 128, required"
            }
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if serializer.passwords_do_not_match():
                return Response(data={"error": "passwords are not matching"}, status=status.HTTP_400_BAD_REQUEST)
            if serializer.email_is_registerd():
                return Response(data={"error": "email is already registered"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.to_capitalize()
            serializer.save()
            return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersListAPIView(ListAPIView):
    queryset = MainUser.objects.filter(is_staff=False, is_active=True)
    serializer_class = UsersListSerializer


class UserDetailsAPIView(RetrieveAPIView):
    queryset = MainUser.objects.filter(is_staff=False, is_active=True)
    serializer_class = UserDetailsSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        try:
            user = MainUser.objects.get(pk=pk)
        except MainUser.DoesNotExist:
            return Response(data={"error": "not found"}, status=status.HTTP_404_NOT_FOUND) 
        else:
            user_serializer = self.serializer_class(instance=user)
            posts = Post.objects.filter(author=user)
            posts_serializer = UsersPostsListSerializer(instance=posts, many=True)
            data = {
                "object": user_serializer.data,
                "posts": posts_serializer.data
                }
            return Response(data=data, status=status.HTTP_200_OK)


class UserUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    model = MainUser
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        return user

    def get(self, request):
        self.object = self.get_object()
        if self.object:
            ser = self.serializer_class(instance=self.object)
            return Response(ser.data, status=status.HTTP_200_OK)
        return self.object

    def put(self, request):
        self.object = self.get_object()
        serializer = self.serializer_class(instance=self.object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        self.object = self.get_object()
        serializer = self.serializer_class(instance=self.object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        self.object = self.get_object()
        self.object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPasswordUpdateAPIView(UpdateAPIView):
    model = MainUser
    serializer_class = UserPasswordUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        return user
    
    def get(self, request):
        data = {
            "information": "update MainUser password",
            "fields": {
                "password": "old password", 
                "new_password": "new password",
                "password_confirmation": "password confirmation",
            }
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        self.object = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.validated_data.get("password")):
                return Response(data={"error": "wrong password"}, status=status.HTTP_400_BAD_REQUEST)
            elif serializer.validated_data.get("new_password") != serializer.validated_data.get("password_confirmation"):
                return Response(data={"error": "passwords do not match"})
            serializer.save(self.object)
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)