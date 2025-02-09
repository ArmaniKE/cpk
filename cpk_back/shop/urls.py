from django.urls import path

from shop.views import get_all_categories

urlpatterns = [
    path('categories', get_all_categories)
]