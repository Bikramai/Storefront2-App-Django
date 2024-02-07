import collections
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework import status
from django.db.models.aggregates import Count
from .models import Product, Collection
from .serializers import CollectionSerializer, ProductSerializer


# Get Method Class
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()

    # def get_serializer(self, *args, **kwargs):
    #     return ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=id)
        if Product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted becauseit is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    

class CollectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.annotate(
        products_count=Count('products'))
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=id)
        if Collection.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted becauseit is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


