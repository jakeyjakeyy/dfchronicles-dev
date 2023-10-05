from rest_framework.views import APIView
from rest_framework.response import Response
import helpers
from .models import User

import xml.etree.ElementTree as ET
import json


# Create your views here.

class WhoAmI(APIView):
    def get(self, request):
        return Response({'user': request.user.id})

class ProcessXML(APIView):
    def post(self, request):
        legends = request.FILES['legends']
        legends_tree = ET.parse(legends)
        legends_root = legends_tree.getroot()
        # Upload to DB
        helpers.XMLToDB(legends_root, request.user)

        legendsplus = request.FILES['legendsplus']
        legendsplus_tree = ET.parse(legendsplus)
        # helper file

        return Response({'message': 'Archive created'})
    