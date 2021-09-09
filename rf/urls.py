from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *

router = routers.DefaultRouter()

router.register('que', RfQuestionBankViewSet)
router.register('room', RfRoomDetailViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
