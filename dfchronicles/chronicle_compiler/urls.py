from django.urls import path

from .views import ProcessXML, WhoAmI, Worlds, Generate

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("token", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("generate", Generate.as_view(), name="generate"),
]
