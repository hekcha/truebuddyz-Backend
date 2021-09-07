from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *

router = routers.DefaultRouter()

router.register('que', YouLookLikeViewSet)
router.register('randque', YouLookLikeRandomViewSet)
router.register('score', YouLookLikeScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
