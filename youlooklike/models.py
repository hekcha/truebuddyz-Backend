from django.db import models


class YouLookLike(models.Model):
    category=models.CharField(max_length=30)
    
    que=models.CharField(max_length=200)
    optionA=models.CharField(max_length=150)
    optionB=models.CharField(max_length=150)
    optionC=models.CharField(max_length=150,blank=True,null=True)
    optionD=models.CharField(max_length=150,blank=True,null=True)
    image=models.CharField(max_length=600,blank=True,null=True)


class YouLookLikeResult(models.Model):
    category=models.CharField(max_length=30)
    name=models.CharField(max_length=40)
    image=models.CharField(max_length=600)
    text=models.CharField(max_length=400)
