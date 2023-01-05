from rest_framework import serializers
from .models import MainUser

from django.contrib.auth.models import User

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from rest_framework.response import Response
from rest_framework import status

class UserCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, min_length=8)
    password2 = serializers.CharField(max_length=128, min_length=8)

    class Meta:
        model = MainUser
        fields = (
            "first_name",
            "last_name",
            "username", 
            "email",
            "password1", 
            "password2"
            )

    def to_capitalize(self):
        first_name = self.validated_data.get("first_name")
        last_name = self.validated_data.get("last_name")
        if first_name:
            self.validated_data["first_name"] = first_name.capitalize()
        if last_name:
            self.validated_data["last_name"] = last_name.capitalize()

    def _check_email_exists(self):
        email = self.validated_data.get("email")
        if MainUser.objects.filter(email=email).exists():
            return True
        return False

    def _check_email_is_real(self):
        email = self.validated_data.get("email")
        if not email:
            return True
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def _are_passwords_matching(self):
        password1 = self.validated_data.get("password1")
        password2 = self.validated_data.get("password2")
        if password1 == password2:
            return True
        return False

    def check_data_is_correct(self):
        if not self._are_passwords_matching():
            return Response(data={"error": "passwords are not matching"}, status=status.HTTP_400_BAD_REQUEST)
        if self._check_email_exists():
            return Response(data={"error": "email is already registered"}, status=status.HTTP_400_BAD_REQUEST)
        if not self._check_email_is_real():
            return Response(data={"error": "email is not real"}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        first_name = validated_data.get("first_name") if validated_data.get("first_name") else ""
        last_name = validated_data.get("last_name") if validated_data.get("last_name") else ""
        email = validated_data.get("email") if validated_data.get("email") else ""
        username = validated_data.get("username")
        password = validated_data.get("passwrod1")
        user = MainUser.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )
        user.set_password(raw_password=password)
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = (
            "id",
            "image", 
            "first_name", 
            "last_name", 
            "username", 
            "email"
            )

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = (
            "id",
            "image", 
            "username"
            )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email"
            )    