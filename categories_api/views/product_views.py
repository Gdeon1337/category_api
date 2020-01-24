from rest_framework import viewsets
from rest_framework.response import Response

from categories_api.models import Products, CategoryAttributes
from categories_api.serializers import ProductsSerializer


class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    def list(self, request, *args, **kwargs):
        category_id = request.query_params.get('category_id')
        price = request.query_params.get('price')
        products = self.get_queryset()
        attributes = []
        if category_id:
            attributes = CategoryAttributes.objects.filter(category_id=category_id).all()
            products = products.filter(category_id=category_id)
        if price:
            min_price, max_price = price.split('-')
            products = products.filter(price__range=(float(min_price), float(max_price)))
        for attribute in attributes:
            attribute_filter_value = request.query_params.get(f'f[{attribute.attribute.id}]')
            if attribute_filter_value:
                products = products.filter(
                    productvalues__value__attribute__id=attribute.attribute.id,
                    productvalues__value__value__data=attribute_filter_value
                    .replace('f[', '').replace(']', '')
                )
                continue
            attribute_filter_value = request.query_params.get(f'fr[{attribute.attribute.id}]')
            if attribute_filter_value:
                attribute_filter_value = attribute_filter_value.replace('fr[', '').replace(']', '')
                min_value, max_value = attribute_filter_value.split('-')
                products = products\
                    .filter(productvalues__value__attribute__id=attribute.attribute.id)\
                    .filter(productvalues__value__value__data__range=(float(min_value), float(max_value)))
        serializer = self.get_serializer(products.all(), many=True)
        return Response(serializer.data)
