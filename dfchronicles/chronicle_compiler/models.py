from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Generations(models.Model):
    user = models.ForeignKey(User, related_name='generations', null=True, on_delete=models.SET_NULL)
    object = models.CharField()
    prompt = models.CharField()
    response = models.CharField()
    time = models.DateTimeField(auto_now_add=True)