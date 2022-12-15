from django.db import models
from django.contrib.auth.models import User


class MainUser(User):
    image = models.ImageField(upload_to="users_images", null=True, blank=True, default="default_images/avatar.png")