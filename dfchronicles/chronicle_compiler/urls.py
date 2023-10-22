from django.urls import path

from .views import ProcessXML, WhoAmI, Login

urlpatterns = [
    path('process-xml', ProcessXML.as_view(), name='process-xml'),
    path('whoami', WhoAmI.as_view(), name='whoami'),
    path('token', Login.as_view(), name='token'),
]