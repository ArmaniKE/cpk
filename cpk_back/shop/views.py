from django.contrib.sessions.serializers import JSONSerializer
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Category
from shop.serializers import CategorySerializer, CreateCategorySerializer, UpdateCategorySerializer


# Create your views here.
class CategoryAPI(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        serializer = CreateCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class CategoryDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk)

        if category:
            serializer = CategorySerializer(category)
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse({'error': 'Category not found'}, status=404)

    def put(self, request, pk):
        category = self.get_object(pk)

        if category is None:
            return JsonResponse({'error': 'Category not found'}, status=404)

        serializer = UpdateCategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        category = self.get_object(pk)

        if category is None:
            return JsonResponse({'error': 'Category not found'}, status=404)

        category.delete()
        return JsonResponse({'message': 'Category deleted'}, status=204)
