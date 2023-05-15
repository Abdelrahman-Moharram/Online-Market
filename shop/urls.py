from django.urls import include, path
from rest_framework import routers
from .views import *

app_name = 'shops'


router = routers.DefaultRouter()
router.register('shop-owner',ShopOwner_ViewSet)
router.register('',Shop_ViewSet)


urlpatterns =[
    path('', include(router.urls)),
]