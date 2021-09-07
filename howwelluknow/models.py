from django.db import models

class HowWellUKnow(models.Model):
    category=models.CharField(max_length=20)
    que=models.CharField(max_length=300)
    optionA=models.CharField(max_length=50)
    optionB=models.CharField(max_length=50)
    optionC=models.CharField(max_length=50)
    optionD=models.CharField(max_length=50)
    ans=models.IntegerField()
    image=models.CharField(max_length=50)

class HowWellUKnowScore(models.Model):
    category=models.CharField(max_length=20)
    score=models.IntegerField()
    message=models.CharField(max_length=100)
    image=models.CharField(max_length=400)

