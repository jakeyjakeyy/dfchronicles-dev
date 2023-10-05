from django.urls import path

from . import views

urlpatterns = [
    path('', views.test_data, name='test_data')
]