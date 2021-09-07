from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *

router = routers.DefaultRouter()

router.register('que', QuizViewSet)
router.register('quebank', QuizQuestionBankViewSet)
router.register('resp', QuizResponseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
