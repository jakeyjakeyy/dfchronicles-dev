from rest_framework.views import APIView
from rest_framework.response import Response
from chronicle_compiler import models
from utils import savedb as save
from utils import linkfkey as link
import time
import logging
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import JSONRenderer
from .serializers import *

import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

# Create your views here.

class WhoAmI(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({'username': user.username})
        else:
            return Response({'username': 'Guest'})
        
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
        with open('log.txt', 'w') as log:
            log.write('-----Saving legends.XML-----\n')
        fkeys = save.SaveLegends(legends_root, world)
        with open('log.txt', 'a') as log:
            log.write('-----Saving legends_plus.XML-----\n')
        fkeysplus = save.SaveLegends(legendsplus_root, world)

        # Save all missing foreign keys
        with open('log.txt', 'a') as log:
            log.write('-----Saving missing foreign keys-----\n')
        with open('timer.txt', 'a') as timer:
            start_time = time.perf_counter()
            link.link_fkeys(fkeys, world)
            end_time = time.perf_counter()
            timer.write('Missing fkeys: ' + str(end_time - start_time) + '\n')
            start_time = time.perf_counter()
            link.link_fkeys(fkeysplus, world)
            end_time = time.perf_counter()
            timer.write('Missing fkeys plus: ' + str(end_time - start_time) + '\n')

        return Response({'message': 'Archive created'})
    
class Worlds(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({'message': 'Invalid token'})
        
        if request.data['request'] == 'worlds':
            worlds = models.World.objects.filter(owner=user)
            serializer = WorldsSerializer(worlds, many=True)
            json = JSONRenderer().render(serializer.data)
            return Response(json)
        elif request.data['request'] == 'world':
            id = request.data['id']
            world = models.World.objects.get(id=id)
            if 'category' not in request.data:
                serializer = WorldsSerializer(world)
                json = JSONRenderer().render(serializer.data)
                return Response(json)
            match request.data['category']:
                case 'Artifacts':
                    if 'object' in request.data:
                        artifact = models.Artifact.objects.get(world=world, id=request.data['object'])
                        serializer = ArtifactSerializer(artifact)
                        json = JSONRenderer().render(serializer.data)
                        return Response(json)
                    artifacts = models.Artifact.objects.filter(world=world)
                    serializer = ArtifactsSerializer(artifacts, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Entities/Governments':
                    entities = models.Entities.objects.filter(world=world)
                    serializer = EntitiesSerializer(entities, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Populations':
                    populations = models.EntityPopulations.objects.filter(world=world)
                    serializer = EntityPopulationsSerializer(populations, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Occasions':
                    occasions = models.Occasion.objects.filter(world=world)
                    serializer = OccasionsSerializer(occasions, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Historical Eras':
                    eras = models.HistoricalEras.objects.filter(world=world)
                    serializer = ErasSerializer(eras, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Historical Event Collections':
                    collections = models.HistoricalEventCollections.objects.filter(world=world)
                    serializer = EventCollectionsSerializer(collections, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Historical Events':
                    events = models.HistoricalEvents.objects.filter(world=world)
                    serializer = HistoricalEventsSerializer(events, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Historical Figures':
                    figures = models.HistoricalFigures.objects.filter(world=world)
                    serializer = HistoricalFiguresSerializer(figures, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Regions':
                    regions = models.Regions.objects.filter(world=world)
                    serializer = RegionsSerializer(regions, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Sites':
                    sites = models.Sites.objects.filter(world=world)
                    serializer = SitesSerializer(sites, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Structures':
                    structures = models.Structures.objects.filter(world=world)
                    serializer = StructuresSerializer(structures, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Underground Regions':
                    regions = models.UndergroundRegions.objects.filter(world=world)
                    serializer = UndergroundRegionsSerializer(regions, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Written Contents':
                    contents = models.WrittenContents.objects.filter(world=world)
                    serializer = WrittenContentsSerializer(contents, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'World Constructions':
                    constructions = models.WorldConstruction.objects.filter(world=world)
                    serializer = WorldConstructionsSerializer(constructions, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Landmasses':
                    landmasses = models.Landmass.objects.filter(world=world)
                    serializer = LandmassesSerializer(landmasses, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Mountain Peaks':
                    peaks = models.MountainPeak.objects.filter(world=world)
                    serializer = MountainPeaksSerializer(peaks, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case 'Plots':
                    plots = models.IntriguePlot.objects.filter(world=world)
                    serializer = IntriguePlotsSerializer(plots, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                    