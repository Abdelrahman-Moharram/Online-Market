from rest_framework import serializers
from .models import *

class ShopOwner_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = ShopOwner
        fields = ('id','user', 'shop_name',)
class Shop_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
class Shop_Employee_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = Shop_Employee
        fields = '__all__'