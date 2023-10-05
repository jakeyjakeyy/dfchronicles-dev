from rest_framework.views import APIView
from rest_framework.response import Response
import helpers

import xml.etree.ElementTree as ET
import json


# Create your views here.

class ProcessXML(APIView):
    def post(self, request):
        legends = request.FILES['legends']
        legends_tree = ET.parse(legends)
        legends_root = legends_tree.getroot()
        # Parse to JSON
        legends_parsed = helpers.ParseXML(legends_root)
        legends_json = json.dumps(legends_parsed, indent=2, sort_keys=True)
        print(legends_json, file=open('legends_parsed.json', 'a'))

        legendsplus = request.FILES['legendsplus']
        legendsplus_tree = ET.parse(legendsplus)
        # helper file

        return Response({'message': 'Archive created'})
    