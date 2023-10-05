from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


# Create your views here.

@api_view(['GET'])
def test_data(request):
    data = {
        'message': 'Hello World!'
    }
    return Response(data)

@api_view(['GET'])
def world_data(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
