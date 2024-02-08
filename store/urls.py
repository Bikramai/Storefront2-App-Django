from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
# from pprint import pprint


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
# pprint(router.urls) if you want to print in terminal 


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('collections', views.ReviewViewSet, basename='product-reviews')

# URLConf
urlpatterns = router.urls + products_router.urls

