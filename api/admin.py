from django.contrib import admin

from .models import Category, Post, FavoritePost, Comment

class AdminCategory(admin.ModelAdmin):
    list_display = (
        "name", 
        "slug"
    )
    search_fields = (
        "name",
    )


class AdminPost(admin.ModelAdmin):
    list_display = (
        "title", 
        "author",
        "category",
        "created_at",
        "modified_at"
    )
    list_filter = (
        "title",
        "author",
        "category",
        "created_at"
    )
    search_fields = (
        "title",
        "author"
    )


class AdminComment(admin.ModelAdmin):
    list_display = (
        "post",
        "author",
        "text"
    )
    list_filter = (
        "post",
        "author",
        "created_at"
    )
    search_fields = (
        "post",
        "author",
        "text"
    )

admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)