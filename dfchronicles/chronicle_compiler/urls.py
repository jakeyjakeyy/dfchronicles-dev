from django.urls import path

from .views import ProcessXML, WhoAmI, Worlds

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('process-xml', ProcessXML.as_view(), name='process-xml'),
    path('whoami', WhoAmI.as_view(), name='whoami'),
    path('token', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('worlds', Worlds.as_view(), name='worlds'),
]