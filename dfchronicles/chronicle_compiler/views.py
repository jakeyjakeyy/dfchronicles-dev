from rest_framework.views import APIView
from rest_framework.response import Response
from chronicle_compiler import models
from utils import savedb as save
from utils import linkfkey as link
import time

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
        world = save.SaveWorld(legendsplus_root, request.user)
        # Get all data from legends and save to DB.
        open('log.txt', 'a').write('-----Saving legends.XML-----\n')
        fkeys = save.SaveLegends(legends_root, world)
        open('log.txt', 'a').write('-----Saving legends_plus.XML-----\n')
        fkeysplus = save.SaveLegends(legendsplus_root, world)

        # Save all missing foreign keys
        open('log.txt', 'a').write('-----Saving missing foreign keys-----\n')
        start_time = time.time()
        link.link_fkeys(fkeys, world)
        end_time = time.time()
        open('timer.txt', 'a').write('Missing fkeys: ' + str(end_time - start_time) + '\n')
        start_time = time.time()
        link.link_fkeys(fkeysplus, world)
        end_time = time.time()
        open('timer.txt', 'a').write('Missing fkeys plus: ' + str(end_time - start_time) + '\n')

        return Response({'message': 'Archive created'})
    