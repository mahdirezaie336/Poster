from django.urls import path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', api_home),
    # path('posts/', api_post_list),
    # path('posts/<int:pk>/', api_post_detail),
    # path('posts/<int:pk>/images/', api_post_image_list),
] + router.urls
