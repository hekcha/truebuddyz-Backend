from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('rating', RatingViewSet)

router.register('entertainment', EntertainmentViewSet)
router.register('entresult', EntertainmentResultViewSet)

router.register('quiz', QuizViewSet)
router.register('quizquebank', QuizQuestionBankViewSet)
router.register('quizresp', QuizResponseViewSet)

router.register('rf', RfQuestionBankViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
