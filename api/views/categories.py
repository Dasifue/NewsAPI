from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Category
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from ..serializers.categories_serializer import (
    CategoresListSerializer,
    CategoryCreateSerializer, 
    CategoryDetailsSerializer
    )

class CategoriesListAPIView(ListAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategoresListSerializer


class CategoryCreateAPIView(CreateAPIView):
    model = Category
    serializer_class = CategoryCreateSerializer
    permission_classes = (IsAuthenticated,)


class CategoryDetailsUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    model = Category
    queryset = Category.objects.filter()
    serializer_class = CategoryDetailsSerializer
    lookup_field = "slug"
    permission_classes = (IsAdminUser,)

    
    
