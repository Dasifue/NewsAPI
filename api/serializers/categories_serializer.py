from rest_framework.serializers import ModelSerializer

from ..models import Category

import random

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name","slug")


class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)

    def _set_title(self):
        name = self.validated_data.get("name").capitalize()
        self.validated_data["name"] = name

    def _set_slug(self):
        name = self.validated_data.get("name").lower()
        name = name.replace(" ", "_")
        coding = coding = random.randrange(1000, 99999, 1)
        slug = f"{name}{coding}"
        self.validated_data["slug"] = slug

    def create(self):
        self._set_title()
        self._set_slug()
        name = self.validated_data.get("name")
        slug = self.validated_data.get("slug")
        Category.objects.create(
            name = name,
            slug = slug
        )


