from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ProductCategory, Product
from .Serializer import *
from rest_framework.views import APIView

class Products_viewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_Serilizer


class Categories(APIView):
    def get(self, request):
        cat = ProductCategory.objects.all()
        cats = Product_Serilizer(cat, many=True)
        return Response(cats.data, status=status.HTTP_200_OK)
    