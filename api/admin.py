from django.contrib import admin

from .models import Category, Post, FavoritePost, Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(FavoritePost)
admin.site.register(Comment)