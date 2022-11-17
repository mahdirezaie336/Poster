from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from posts.models import Post


@api_view(['GET'])
def api_home(request):
    """
    This is the home page for the API
    """
    params = request.query_params
    print(params)

    # Get
    return Response(status=status.HTTP_201_CREATED)
