from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *


router = routers.DefaultRouter()

router.register('user', UserViewSet)
router.register('trnd', TrendingViewSet)
router.register('new', NewGamesViewSet)
router.register('feedback', FeedbackViewSet)
router.register('contribution', ContributionViewSet)
router.register('rating', RatingViewSet)
router.register('data', GamesDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
