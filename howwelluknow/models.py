from django.db import models

class HowWellUKnow(models.Model):
    category=models.CharField(max_length=30)
    que=models.CharField(max_length=300)
    optionA=models.CharField(max_length=50)
    optionB=models.CharField(max_length=50)
    optionC=models.CharField(max_length=50)
    optionD=models.CharField(max_length=50)
    ans=models.IntegerField()
    image=models.CharField(max_length=600)

class HowWellUKnowScore(models.Model):
    category=models.CharField(max_length=30)
    score=models.IntegerField()
    complement=models.CharField(max_length=30)
    message=models.CharField(max_length=500)
    image=models.CharField(max_length=600)

