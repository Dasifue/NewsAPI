from rest_framework import serializers
from .models import MainUser

from django.contrib.auth.models import User

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UserCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, min_length=8)
    password2 = serializers.CharField(max_length=128, min_length=8)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username", 
            "email",
            "password1", 
            "password2"
            )
            

    def are_passwords_matching(self):
        password1 = self.validated_data.get("password1")
        password2 = self.validated_data.get("password2")
        if password1 == password2:
            return True
        return False

    def to_capitalize(self):
        first_name = self.validated_data.get("first_name")
        last_name = self.validated_data.get("last_name")
        if first_name:
            self.validated_data["first_name"] = first_name.capitalize()
        if last_name:
            self.validated_data["last_name"] = last_name.capitalize()

    def check_email_exists(self):
        email = self.validated_data.get("email")
        if MainUser.objects.filter(email=email).exists():
            return True
        return False

    def check_email_is_real(self):
        email = self.validated_data.get("email")
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def create(self, validated_data):
        first_name = validated_data.get("first_name") if validated_data.get("first_name") else ""
        last_name = validated_data.get("last_name") if validated_data.get("last_name") else ""
        email = validated_data.get("email") if validated_data.get("email") else ""
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = validated_data.get("username"),
            email = email
        )
        user.set_password(validated_data.get("password1"))
        return user

