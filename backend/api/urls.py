from django.urls import path
from rest_framework import routers

from .views import PostViewSet, api_home

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', api_home),
] + router.urls
