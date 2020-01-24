from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductsView, CategoriesView

router = DefaultRouter()
router.register(r'category', CategoriesView, basename='category')
router.register(r'product', ProductsView, basename='product')
urlpatterns = router.urls
