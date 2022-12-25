from django.urls import path

from .views.categories import ListCreateCategoriesAPIView

app_name = "api"

urlpatterns = [
    path("categories/list/create", ListCreateCategoriesAPIView.as_view(), name="categories")
]