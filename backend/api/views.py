from django.http import JsonResponse
import django


def api_home(request, *args, **kwargs):
    body = request.body
    print(body)
    print(args)
    print(request.GET)
    return JsonResponse({"message": "Hello, world!"})
