from django.db import models
from accounts.models import User
import uuid

class ShopOwner(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.user)

class Shop(models.Model):
    def imagesave(instance,filename):
        imagename , extension = filename.split(".")
        return "shops/%s.%s"%(instance.shop_id,extension)

    shop_id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False, unique=True)
    shop_owner      = models.OneToOneField(ShopOwner, on_delete=models.PROTECT)
    shop_name       = models.CharField(max_length=20, unique=True)
    Created_date    = models.DateField(auto_now=False, blank=True, null=True)
    location        = models.CharField(max_length=40)
    shop_image      = models.ImageField(upload_to=imagesave)
    def __str__(self) -> str:
        return self.shop_name

class Shop_Employee(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    shop            = models.ForeignKey(Shop, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.user) + " works at " +self.shop.shop_name