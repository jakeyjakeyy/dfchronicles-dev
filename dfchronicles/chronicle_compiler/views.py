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
import openai
import os
from dotenv import load_dotenv
import tiktoken

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

# Create your views here.


class WhoAmI(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({"username": user.username})
        else:
            return Response({"username": "Guest"})


class ProcessXML(APIView):
    def post(self, request):
        # pull root files
        legends = request.FILES["legends"]
        legends_tree = ET.parse(legends)
        legends_root = legends_tree.getroot()

        legendsplus = request.FILES["legendsplus"]
        legendsplus_tree = ET.parse(legendsplus)
        legendsplus_root = legendsplus_tree.getroot()

        # Get world from legends_plus and save to DB. This is our reference point.
        world = save.SaveWorld(legendsplus_root, request.user)
        # Get all data from legends and save to DB.
        with open("log.txt", "w") as log:
            log.write("-----Saving legends.XML-----\n")
        fkeys = save.SaveLegends(legends_root, world)
        with open("log.txt", "a") as log:
            log.write("-----Saving legends_plus.XML-----\n")
        fkeysplus = save.SaveLegends(legendsplus_root, world)

        # Save all missing foreign keys
        with open("log.txt", "a") as log:
            log.write("-----Saving missing foreign keys-----\n")
        with open("timer.txt", "a") as timer:
            start_time = time.perf_counter()
            link.link_fkeys(fkeys, world)
            end_time = time.perf_counter()
            timer.write("Missing fkeys: " + str(end_time - start_time) + "\n")
            start_time = time.perf_counter()
            link.link_fkeys(fkeysplus, world)
            end_time = time.perf_counter()
            timer.write("Missing fkeys plus: " + str(end_time - start_time) + "\n")

        return Response({"message": "Archive created"})


class Worlds(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"message": "Invalid token"})

        if request.data["request"] == "worlds":
            worlds = models.World.objects.filter(owner=user)
            serializer = WorldsSerializer(worlds, many=True)
            json = JSONRenderer().render(serializer.data)
            return Response(json)
        elif request.data["request"] == "world":
            id = request.data["id"]
            world = models.World.objects.get(id=id)
            if "category" not in request.data:
                serializer = WorldsSerializer(world)
                json = JSONRenderer().render(serializer.data)
                return Response(json)
            match request.data["category"]:
                case "Artifacts":
                    if "object" in request.data:
                        artifact = models.Artifact.objects.get(
                            world=world, id=request.data["object"]
                        )
                        serializer = ArtifactSerializer(artifact)
                        json = JSONRenderer().render(serializer.data)
                        return Response(json)
                    artifacts = models.Artifact.objects.filter(world=world)
                    serializer = ArtifactsSerializer(artifacts, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Entities/Governments":
                    if "object" in request.data:
                        entity = models.Entities.objects.get(
                            world=world, id=request.data["object"]
                        )
                        serializer = EntitySerializer(entity)
                        json = JSONRenderer().render(serializer.data)
                        return Response(json)
                    entities = models.Entities.objects.filter(world=world)
                    serializer = EntitiesSerializer(entities, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Populations":
                    populations = models.EntityPopulations.objects.filter(world=world)
                    serializer = EntityPopulationsSerializer(populations, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Occasions":
                    if "object" in request.data:
                        occasion = models.Occasion.objects.get(
                            id=request.data["object"]
                        )
                        serializer = OccasionSerializer(occasion)
                        json = JSONRenderer().render(serializer.data)
                        return Response(json)
                    occasions = models.Occasion.objects.filter(world=world)
                    serializer = OccasionsSerializer(occasions, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Historical Eras":
                    eras = models.HistoricalEras.objects.filter(world=world)
                    serializer = ErasSerializer(eras, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Historical Event Collections":
                    if "object" in request.data:
                        collection = models.HistoricalEventCollections.objects.get(
                            world=world, id=request.data["object"]
                        )
                        serializer = EventCollectionSerializer(collection)
                        json = JSONRenderer().render(serializer.data)
                        return Response(json)
                    collections = models.HistoricalEventCollections.objects.filter(
                        world=world
                    )
                    serializer = EventCollectionsSerializer(collections, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Historical Events":
                    if "object" in request.data:
                        event = models.HistoricalEvents.objects.get(
                            world=world, id=request.data["object"]
                        )
                        serializer = HistoricalEventSerializer(event)
                        json = JSONRenderer().render(serializer.data)
                        return Response(json)
                    events = models.HistoricalEvents.objects.filter(world=world)
                    serializer = HistoricalEventsSerializer(events, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Historical Figures":
                    if "object" in request.data:
                        figure = models.HistoricalFigures.objects.get(
                            world=world, id=request.data["object"]
                        )
                        serializer = HistoricalFigureSerializer(figure)
                        json = JSONRenderer().render(serializer.data)
                        return Response(json)
                    figures = models.HistoricalFigures.objects.filter(world=world)
                    serializer = HistoricalFiguresSerializer(figures, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Regions":
                    if "object" in request.data:
                        region = models.Regions.objects.get(
                            world=world, id=request.data["object"]
                        )
                        serializer = RegionSerializer(region)
                        json = JSONRenderer().render(serializer.data)
                        return Response(json)
                    regions = models.Regions.objects.filter(world=world)
                    serializer = RegionsSerializer(regions, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Sites":
                    if "object" in request.data:
                        site = models.Sites.objects.get(
                            world=world, id=request.data["object"]
                        )
                        serializer = SiteSerializer(site)
                        json = JSONRenderer().render(serializer.data)
                        return Response(json)
                    sites = models.Sites.objects.filter(world=world)
                    serializer = SitesSerializer(sites, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Structures":
                    structures = models.Structures.objects.filter(world=world)
                    serializer = StructuresSerializer(structures, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Underground Regions":
                    regions = models.UndergroundRegions.objects.filter(world=world)
                    serializer = UndergroundRegionsSerializer(regions, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Written Contents":
                    contents = models.WrittenContents.objects.filter(world=world)
                    serializer = WrittenContentsSerializer(contents, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "World Constructions":
                    constructions = models.WorldConstruction.objects.filter(world=world)
                    serializer = WorldConstructionsSerializer(constructions, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Landmasses":
                    landmasses = models.Landmass.objects.filter(world=world)
                    serializer = LandmassesSerializer(landmasses, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Mountain Peaks":
                    peaks = models.MountainPeak.objects.filter(world=world)
                    serializer = MountainPeaksSerializer(peaks, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                case "Plots":
                    plots = models.IntriguePlot.objects.filter(world=world)
                    serializer = IntriguePlotsSerializer(plots, many=True)
                    json = JSONRenderer().render(serializer.data)
                    return Response(json)
                # case 'Written Content Reference':
                #     ref = models.WrittenContentReference.objects.filter(world=world, id=request.data['object'])
                #     serializer = WrittenContentReferenceSerializer(ref)
                #     json = JSONRenderer().render(serializer.data)
                #     return Response(json)


class Generate(APIView):
    authentication_classes = [JWTAuthentication]
    prompt = 'In a realm shaped by the intricate mechanics of "Dwarf Fortress", imagine yourself as a skilled archivist dedicated to preserving the rich tapestry of events and history in this unique world. Your mission is to craft an engaging and enthralling narrative using the information at your disposal. While remaining true to the established facts, infuse the story with vivid details that may not explicitly be provided to you, in order to captivate the reader. The story should take readers on a journey through this extraordinary realm.'
    # prompt = "Imagine yourself as a skilled archivist in the unique world of 'Dwarf Fortress'. Make no mention magic. Your mission is to create an engaging narrative that captures the essence of this extraordinary tale. While staying true to the established facts, add vivid details to captivate the reader. Take your readers on a journey through this realm, and make the story come alive. If an object has two names, include the second Dwarvish name."
    # prompt = "Imagine yourself as a skilled archivist in the unique setting of Dwarf Fortress a realm where the rules and constraints shape everything. Your mission is to create an engaging narrative that captures the essence of this extraordinary world. While staying true to the established facts, add vivid details to captivate the reader. Take your readers on a journey through this realm, and make the story come alive. If an object has two names, include the second Dwarvish name."
    # prompt = "Imagine you're an archivist from the game Dwarf Fortress. Do not mention magic. Your task is to craft an engaging narrative that brings this extraordinary realm to life, while stricly describing only the information provided. Feel free to embellish information to add description, only if the description further describes the established facts. Infuse vivid details to captivate readers and take them on a journey through this realm. If an object has two names, include the second Dwarvish name."
    # prompt = "Tell me a captivating story that revolves around this historical event. Introduce memorable characters, describe the dramatic events that unfolded, and let the rich lore of Dwarf Fortress come alive. Convey the bravery, the turmoil, and the unforgettable moments that defined this moment in the kingdom's history (whether trivial or pivitol in the course of history). Your words have the power to make the past come alive once more."
    # "Act like an archivist from a fantasy realm who is chronicling events and the history of your world to provide an exciting recount of the information provided. Write a detailed story based on the information provided. Fill in details to make the story interesting while maintaining the overall facts provided. Write the story from a third person perspective."

    def post(self, request):
        user = request.user
        model = "gpt-3.5-turbo"
        # model = "gpt-4-1106-preview"
        maxTokens = 3000
        if model == "gpt-4-1106-preview":
            maxTokens = 4000
        if not user.is_authenticated:
            return Response({"message": "Invalid token"})

        if request.data["request"] == "generate":
            enc = tiktoken.encoding_for_model(model)
            if len(enc.encode(request.data["prompt"])) > maxTokens:
                return Response({"message": f"Prompt too long {len(enc.encode(request.data['prompt']))} of 3000 tokens"})
            try:
                completion = openai.ChatCompletion.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": self.prompt,
                        },
                        {"role": "user", "content": request.data["prompt"]},
                    ],
                    temperature=0.7,
                    top_p=0.8,
                )
            except openai.error.ServiceUnavailableErrorr:
                return Response({"message": "Service Unavailable"})
            
            # Save Generation to databse
            gen = models.Generations.objects.create(
                user=user, object=request.data["prompt"], prompt=self.prompt, response=completion
            )
            gen.save()
            
            response = completion["choices"][0]["message"]["content"]
            return Response({"generation": response})
            # return Response({"message": "New line test\n\nNew line test"})
