from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Category

from ..serializers.categories_serializer import CategorySerializer, CategoryCreateSerializer

class ListCreateCategoriesAPIView(APIView):

    def get(self, request):
        queryset = Category.objects.all()
        categories = CategorySerializer(instance=queryset, many=True)
        return Response(data=categories.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        if request.user.is_superuser:
            category = CategoryCreateSerializer(data=request.data)
            if category.is_valid():
                category.create()
                return Response(data=category.data, status=status.HTTP_201_CREATED)
            return Response(data={"error": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"error": "must be superuser"}, status=status.HTTP_401_UNAUTHORIZED)
