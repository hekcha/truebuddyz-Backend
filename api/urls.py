from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views.quiz import *
from .views.entertainment import *
from .views.howwelluknow import *
from .views.other import *

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('hwuk', HowWellUKnowViewSet)
router.register('hwuks', HowWellUKnowScoreViewSet)
router.register('trnd', TrendingViewSet)


router.register('feedback', FeedbackViewSet)
router.register('contribution', ContributionViewSet)
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
