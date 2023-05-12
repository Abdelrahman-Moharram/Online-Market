from django.contrib import admin
from .models import ShopOwner, Shop, Shop_Employee


admin.site.register(ShopOwner)
admin.site.register(Shop)
admin.site.register(Shop_Employee)
