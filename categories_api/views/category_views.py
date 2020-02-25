from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.db.models import Count, Prefetch, Q

from categories_api.models import Categories, Values, Attributes, CategoryAttributes, Products
from categories_api.serializers import CategoriesSerializer


class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        attributes = CategoryAttributes.objects.filter(category_id=kwargs.get('pk')).all()
        product_queryset = Products.objects.filter(category_id=kwargs.get('pk'))
        for attribute in attributes:
            attribute_filter_value = request.query_params.get(f'f[{attribute.attribute_id}]')
            if attribute_filter_value:
                product_queryset = product_queryset.filter(
                    productvalues__value__attribute__id=attribute.attribute.id,
                    productvalues__value__value__data=attribute_filter_value.replace('f[', '').replace(']', '')
                )
                continue
            attribute_filter_value = request.query_params.get(f'fr[{attribute.attribute_id}]')
            if attribute_filter_value:
                attribute_filter_value = attribute_filter_value.replace('fr[', '').replace(']', '')
                min_value, max_value = attribute_filter_value.split('-')
                product_queryset = product_queryset \
                    .filter(productvalues__value__attribute__id=attribute.attribute.id) \
                    .filter(productvalues__value__value__data__range=(float(min_value), float(max_value)))
        q_ = Q()
        for product in product_queryset:
            q_ = q_ | Q(productvalues__product_id=product.id)
        queryset = queryset.annotate(count_products=Count('products'))\
            .prefetch_related(
                Prefetch(
                    'attributes',
                    queryset=Attributes.objects.prefetch_related(
                        Prefetch(
                            'values_set',
                            queryset=Values.objects.annotate(count_products=Count('products', filter=q_))
                        )
                    )
                )
            )
        queryset = get_object_or_404(queryset, pk=kwargs.get('pk'))
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        queryset = queryset.annotate(count_products=Count('products'))\
            .prefetch_related(
                Prefetch(
                    'attributes',
                    queryset=Attributes.objects.prefetch_related(
                        Prefetch(
                            'values_set',
                            queryset=Values.objects.annotate(count_products=Count('products'))
                        )
                    )
                )
            )
        serializer = self.get_serializer(queryset.all(), many=True)
        return Response(serializer.data)
