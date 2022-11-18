from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Post
from posts.serializers import PostSerializer
from .rabbitmq import RabbitMQ
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

    def create(self, request, *args, **kwargs):
        # Create a new post
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Create post object from request
        post = Post.objects.get(id=serializer.data['id'])

        # Send the post to the queue
        queue_data = dict(serializer.data)
        queue_data['image-name'] = str(post.image)
        rabbitmq = RabbitMQ()
        rabbitmq.publish(queue_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

