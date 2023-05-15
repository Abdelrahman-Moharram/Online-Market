from django.urls import include, path
from rest_framework import routers
from .views import *

app_name = 'home'


router = routers.DefaultRouter()
router.register('',Products_viewsets)


urlpatterns =[
    path('products', include(router.urls)),
    path('products/category', Categories.as_view()),
]