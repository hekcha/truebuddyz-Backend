from typing import Text
from django.db import models
from django.contrib.auth.models import User

# friends, couple, BFF , happy new year

class RfQuestionBank(models.Model):
    category=models.CharField(max_length=20)
    que=models.CharField(max_length=200,blank=True,null=True)


class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    value=models.IntegerField()
    def __str__(self):
        return self.user.username + " "+str(self.value)


class Feedback(models.Model):
    user=models.CharField(max_length=20)
    rating=models.IntegerField()
    text=models.CharField(max_length=1000)


class Contribution(models.Model):
    user=models.CharField(max_length=20)
    name=models.CharField(max_length=61)
    email=models.EmailField()
    game=models.CharField(max_length=45)
    message=models.CharField(max_length=1000)


class Trending(models.Model):
    rank=models.IntegerField()
    is_active=models.BooleanField(default=False)
    link=models.CharField(max_length=100)
    text=models.CharField(max_length=50)
    image=models.CharField(max_length=300)
