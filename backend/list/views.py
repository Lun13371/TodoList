from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def get_items(request):
    data = [
        {
            'id': 0,
            'name': 'test'
        }
    ]
    return Response(data)