from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Post


@api_view(['GET'])
def api_home(request, *args):
    """
    This is the home page for the API
    """
    body = request.body
    print(body)
    print(args)
    print(request.GET)
    return Response({"message": "Hello, world!"})
