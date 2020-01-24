from django.contrib import admin
from .models import (
    Categories, CategoryAttributes, Products, Attributes, Values, ProductValues
)
# Register your models here.

admin.site.register(Categories)
admin.site.register(CategoryAttributes)
admin.site.register(ProductValues)
admin.site.register(Values)
admin.site.register(Products)
admin.site.register(Attributes)
