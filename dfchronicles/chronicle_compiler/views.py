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

logger = logging.getLogger(__name__)

class Generate(APIView):
    authentication_classes = [JWTAuthentication]
    prompt = 'In a realm shaped by the intricate mechanics of "Dwarf Fortress", imagine yourself as a skilled archivist dedicated to preserving the rich tapestry of events and history in this unique world. Your mission is to craft an engaging and enthralling narrative using the information at your disposal. While remaining true to the established facts, infuse the story with vivid details that may not explicitly be provided to you, in order to captivate the reader. The story should take readers on a journey through this extraordinary realm.'

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
            
            gen = models.Generations.objects.create(
                user=user, object=request.data["prompt"], prompt=self.prompt, response=completion
            )
            gen.save()
            
            response = completion["choices"][0]["message"]["content"]
            return Response({"generation": response})