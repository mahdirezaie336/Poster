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


@api_view(['GET', 'POST'])
def api_post_list(request):
    """
    This is the home page for the API
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def api_post_detail(request, pk):
    """
    This is the home page for the API
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get by id
        if self.kwargs.get('pk'):
            return Post.objects.filter(id=self.kwargs['pk'])
        # Get all
        return Post.objects.all()
