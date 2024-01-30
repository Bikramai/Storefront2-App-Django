from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here. It's function that takes the resquest and return the response
@api_view()
def product_list(request):
    return Response('ok')


@api_view()
def product_detail(request, id):
    return Response(id)
