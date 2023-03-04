from django.db import models
from django.contrib.auth.models import User


class MainUser(User):
    image = models.ImageField(upload_to="users_images", null=True, blank=True, default="default_images/avatar.png")
    role = models.CharField(max_length=254, null=True, blank=True, default="Soft User")
    year_of_birth = models.DateField(null=True, blank=True, default=None)
    age = models.SmallIntegerField(null=True, blank=True, default=None)