from rest_framework import serializers

from ..models import Attributes, Values


class ValuesSerializer(serializers.ModelSerializer):
    count_products = serializers.IntegerField(required=False, read_only=True)
    value = serializers.JSONField(required=False)

    class Meta:
        model = Values
        fields = ('id', 'count_products', 'value', 'attribute_id')


class AttributesSerializer(serializers.ModelSerializer):
    values_set = ValuesSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Attributes
        fields = ('id', 'title', 'values_set')
