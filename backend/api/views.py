from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Post
from posts.serializers import PostSerializer
from django.core.files.storage import default_storage


@api_view(['GET'])
def api_home(request):
    """
    This is the home page for the API
    """
    return Response("Welcome to the API home page")


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get by id
        if self.kwargs.get('pk'):
            return Post.objects.filter(id=self.kwargs['pk'])
        # Get all
        return Post.objects.all()
