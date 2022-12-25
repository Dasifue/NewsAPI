"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import (
    UserCreateAPIView,
    UsersListAPIView,
    UserDetailsAPIView,
    UserUpdateAPIView
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', view=UserCreateAPIView.as_view(), name="register"),
    path('api/user/', include('rest_framework.urls')),
    path('api/users/list', UsersListAPIView.as_view(), name="users_list"),
    path('api/user/details/<int:pk>', UserDetailsAPIView.as_view(), name="user_details"),
    path('api/user/update/<int:pk>', UserUpdateAPIView.as_view(), name="user_update"),
    path('api/', include('api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
