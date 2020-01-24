import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField


class Categories(models.Model):
    title = models.CharField(max_length=16)
    attributes = models.ManyToManyField('Attributes', through='CategoryAttributes')

    def __str__(self):
        return self.title


class Attributes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title


class CategoryAttributes(models.Model):
    priority = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attributes, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.title}__{self.attribute.title}'


class Products(models.Model):
    title = models.CharField(max_length=16)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.title


class Values(models.Model):
    value = JSONField()
    attribute = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    products = models.ManyToManyField('Products', through='ProductValues')

    def __str__(self):
        return f'{self.attribute.title}__{self.value.get("data", "")}'


class ProductValues(models.Model):
    priority = models.IntegerField()

    value = models.ForeignKey(Values, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title}__{self.value.attribute.title}'
