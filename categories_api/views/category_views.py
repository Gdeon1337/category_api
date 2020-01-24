from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.db.models import Count, Prefetch

from categories_api.models import Categories, Values, Attributes
from categories_api.serializers import CategoriesSerializer


class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.annotate(count_products=Count('products'))
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
