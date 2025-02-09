from django.contrib.sessions.serializers import JSONSerializer
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Category
from shop.serializers import CategorySerializer


# Create your views here.
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)