from django.shortcuts import render
from rest_framework import viewsets
from shop.Serializer import *
from shop.models import *

class ShopOwner_ViewSet(viewsets.ModelViewSet):
    queryset = ShopOwner.objects.all()
    serializer_class = ShopOwner_Serilizer

class Shop_ViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = Shop_Serilizer