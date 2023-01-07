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


    def passwords_do_not_match(self):
        password1 = self.validated_data.get("password1")
        password2 = self.validated_data.get("password2")
        if password1 != password2:
            return True

    
    def email_is_registerd(self):
        email = self.validated_data.get("email")
        if MainUser.objects.filter(email=email):
            return True


    def create(self, validated_data):
        first_name = validated_data.get("first_name") if validated_data.get("first_name") else ""
        last_name = validated_data.get("last_name") if validated_data.get("last_name") else ""
        email = validated_data.get("email") if validated_data.get("email") else ""
        username = validated_data.get("username")
        password = validated_data.get("password1")
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


class UserPasswordUpdateSerializer(serializers.Serializer):    
    password = serializers.CharField(max_length=128, min_length=8)
    new_password = serializers.CharField(max_length=128, min_length=8)
    password_confirmation = serializers.CharField(max_length=128, min_length=8)

    def save(self, intance):
        password = self.validated_data.get('new_password')
        intance.set_password(password)
        intance.save()
        return intance