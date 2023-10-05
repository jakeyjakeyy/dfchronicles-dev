from rest_framework.views import APIView
from rest_framework.response import Response

import xml.etree.ElementTree as ET
import json


# Create your views here.

class test_data(APIView):
    def get(self, request):
        data = {
            'message': 'Hello World!'
        }
        return Response(data)


class ProcessXML(APIView):
    def post(self, request):
        legends = request.FILES['legends']
        legends_tree = ET.parse(legends)
        # helper file

        legendsplus = request.FILES['legendsplus']
        legendsplus_tree = ET.parse(legendsplus)
        # helper file

        return Response({'message': 'Archive created'})
    