from django.db import models

class ThisOrThat(models.Model):
    category=models.CharField(max_length=30)
    optionA=models.CharField(max_length=80)
    optionB=models.CharField(max_length=80)

class WouldYouRather(models.Model):
    category=models.CharField(max_length=30,default="all")
    que=models.CharField(max_length=200)
    optionA=models.CharField(max_length=150)
    optionB=models.CharField(max_length=150)
