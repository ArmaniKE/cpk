from rest_framework import serializers

from shop.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent.name', read_only=True)
    # children = serializers.SerializerMethodField(source='children.name', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image_url', 'parent_name')

    # def get_children(self, obj):
    #     if obj.children:
    #         return CategoryNameSerializer(obj.children.all(), many=True).data
    #     return None

# class CategoryNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = 'name',