from django.contrib import admin

# Register your models here.

from .models import MainUser

class AdminMainUser(admin.ModelAdmin):
    list_display = (
        "username",
        "role"
    )
    list_filter = (
        "role",
        "age"
    )
    search_fields = (
        "username",
        "email"
    )

admin.site.register(MainUser, AdminMainUser)