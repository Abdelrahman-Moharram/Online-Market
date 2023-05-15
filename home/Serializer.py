from rest_framework import serializers
from .models import ProductCategory, Product, ProductImage, ProductData, ProductRate

class ProductCategory_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
class Product_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productUUID', 'description', 'ar_description', 'price', 'currency', 'discount', 'stock', 'productCategory', 'shop', 'publisher', 'ProductStars']
        
class ProductImage_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
        
class ProductData_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductData
        fields = '__all__'
        
class ProductRate_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductRate
        fields = '__all__'
        
