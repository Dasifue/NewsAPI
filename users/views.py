from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import MainUser

from .serializers import (
    UserCreateSerializer,
    UsersListSerializer,
    UserDetailsSerializer,
    UserUpdateSerializer
)

class UserCreateAPIView(APIView):

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
        user = UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.check_data_is_correct()
            user.to_capitalize()
            user.create(user.validated_data)
            return Response(data=user.validated_data, status=status.HTTP_201_CREATED)
        return Response(data={"error": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)


class UsersListAPIView(ListAPIView):
    queryset = MainUser.objects.all()#filter(is_staff=False, is_active=True)
    serializer_class = UsersListSerializer


class UserDetailsAPIView(RetrieveAPIView):
    queryset = MainUser.objects.filter(is_staff=False, is_active=True)
    serializer_class = UserDetailsSerializer
    lookup_field = 'pk'


class UserUpdateAPIView(APIView):

    def get(self, request, pk):
        try:
            user = MainUser.objects.get(pk=pk)
            if request.user == user:
                user = UserUpdateSerializer(instance=user)
                return Response(data=user.data, status=status.HTTP_200_OK)
            return Response(data={"error": "not allowed"}, status=status.HTTP_400_BAD_REQUEST)
        except MainUser.DoesNotExist:
            return Response(data={"error": "not found"}, status=status.HTTP_404_NOT_FOUND)