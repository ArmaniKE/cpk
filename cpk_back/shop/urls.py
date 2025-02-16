from django.urls import path

from shop.views import CategoryAPI, CategoryDetailAPI

urlpatterns = [
    path('categories', CategoryAPI.as_view()),
    path('categories/<int:pk>', CategoryDetailAPI.as_view()),
]