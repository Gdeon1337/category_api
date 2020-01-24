from rest_framework import serializers
from .attribute_serializer import AttributesSerializer
from ..models import Categories, CategoryAttributes


class CategoriesSerializer(serializers.ModelSerializer):
    count_products = serializers.IntegerField(required=False, read_only=True)
    attributes = AttributesSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ('id', 'title', 'count_products', 'attributes')
