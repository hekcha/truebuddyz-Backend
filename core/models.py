from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    value = models.IntegerField()


class Feedback(models.Model):
    user = models.CharField(max_length=18)
    rating = models.IntegerField()
    text = models.CharField(max_length=1000)


class Contribution(models.Model):
    user = models.CharField(max_length=18)
    name = models.CharField(max_length=61)
    email = models.EmailField()
    game = models.CharField(max_length=45)
    message = models.CharField(max_length=1300)


class Trending(models.Model):
    rank = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_GradientCard = models.BooleanField(default=True)
    link = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    image = models.CharField(max_length=600)


class NewGames(models.Model):
    rank = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_GradientCard = models.BooleanField(default=True)
    link = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    image = models.CharField(max_length=600)


class GamesData(models.Model):
    game = models.CharField(max_length=50)
    subGame = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    text = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(default=timezone.now)
