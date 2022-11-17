from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Post, PostImage
from posts.serializers import PostSerializer


@api_view(['GET'])
def api_home(request):
    """
    This is the home page for the API
    """
    return Response("Welcome to the API home page")


@api_view(['GET'])
def api_post_list(request):
    """
    This is the home page for the API
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
