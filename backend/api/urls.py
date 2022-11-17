from django.urls import path

from .views import *


urlpatterns = [
    path('', api_home),
    path('posts/', api_post_list),
]
