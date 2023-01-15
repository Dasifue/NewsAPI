from django.db import models
from django.contrib.auth.models import User

from users.models import MainUser

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    author = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.author}/{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class FavoritePost(models.Model):
    Mainuser = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}/{self.post.title}/{self.text[:21]}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"