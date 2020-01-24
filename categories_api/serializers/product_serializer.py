from rest_framework import serializers
from .attribute_serializer import AttributesSerializer, ValuesSerializer
from ..models import Products


class ProductsSerializer(serializers.ModelSerializer):
    values_set = ValuesSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = Products
        fields = ('id', 'title', 'price', 'values_set')
