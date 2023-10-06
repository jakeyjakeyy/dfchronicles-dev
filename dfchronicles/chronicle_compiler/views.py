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
        # pull root files
        legends = request.FILES['legends']
        legends_tree = ET.parse(legends)
        legends_root = legends_tree.getroot()

        legendsplus = request.FILES['legendsplus']
        legendsplus_tree = ET.parse(legendsplus)
        legendsplus_root = legendsplus_tree.getroot()
        
        # Get world from legends_plus and save to DB. This is our reference point.
        world = helpers.SaveWorld(legendsplus_root, request.user)
        # Get all data from legends and save to DB.
        open('log.txt', 'a').write('--------------------Saving legends\n')
        helpers.SaveLegends(legends_root, world)
        open('log.txt', 'a').write('--------------------Saving legends_plus\n')
        helpers.SaveLegends(legendsplus_root, world)

        return Response({'message': 'Archive created'})
    