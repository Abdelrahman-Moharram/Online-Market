from django.db import models
from accounts.models import User
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

from shop.models import Shop, Shop_Employee

class ProductCategory(models.Model):
    def imagesave(instance,filename):
        imagename , extension = filename.split(".")
        return "Category/%s.%s"%(instance.id,extension)
    
    
    title               = models.CharField(max_length=40, verbose_name="Product Category")
    ar_title            = models.CharField(max_length=40, verbose_name="نوع المنتج")
    Category_image      = models.ImageField(upload_to=imagesave, height_field=None, width_field=None)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    productUUID         = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title               = models.TextField(verbose_name="Product Category")
    ar_title            = models.TextField(verbose_name="اسم المنتج")
    price               = models.FloatField()
    currency            = models.CharField(max_length=5)
    ar_description      = models.TextField(null=True, blank=True)
    discount            = models.FloatField()
    stock               = models.IntegerField(default=1)
    productCategory     = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    shop                = models.ForeignKey(Shop, on_delete=models.PROTECT)
    publisher           = models.ForeignKey(Shop_Employee, on_delete=models.PROTECT)
    favourite           = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.title


class ProductImage(models.Model):
    def imagesave(instance,filename):
        imagename , extension = filename.split(".")
        return "Category/%s.%s/"%(instance.id,extension)
    
    image               = models.ImageField(upload_to=imagesave, height_field=None, width_field=None)
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.product.title
class ProductData(models.Model):
    key                 = models.CharField(max_length=40)
    value               = models.TextField()
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.key + " : " + self.value
class ProductRate(models.Model):
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    stars               = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    def __str__(self) -> str:
        return self.product.title + " got " + str(self.stars) +"/5 from " + self.user 