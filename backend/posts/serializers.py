from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'description', 'email', 'state', 'category', 'image']
        read_only_fields = ['id', 'state']
        write_only_fields = ['image']


# class PostImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostImage
#         fields = ['id', 'post', 'image']
