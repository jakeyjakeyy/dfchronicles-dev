from django.urls import path

from .views import ProcessXML

urlpatterns = [
    path('process-xml', ProcessXML.as_view(), name='process-xml'),
]