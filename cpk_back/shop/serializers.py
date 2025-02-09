from rest_framework import serializers

from shop.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent.name', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image_url', 'parent_name')
