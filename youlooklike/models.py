from django.db import models


class YouLookLikeRandom(models.Model):
    category=models.CharField(max_length=30)
    
    que=models.CharField(max_length=200)
    optionA=models.CharField(max_length=80)
    optionB=models.CharField(max_length=80)
    optionC=models.CharField(max_length=80,blank=True,null=True)
    optionD=models.CharField(max_length=80,blank=True,null=True)
    image=models.CharField(max_length=600,blank=True,null=True)

class YouLookLike(models.Model):
    category=models.CharField(max_length=30)
    
    que1=models.CharField(max_length=200)
    option1A=models.CharField(max_length=80)
    option1B=models.CharField(max_length=80)
    option1C=models.CharField(max_length=80,blank=True,null=True)
    option1D=models.CharField(max_length=80,blank=True,null=True)
    image1=models.CharField(max_length=600,blank=True,null=True)

    que2=models.CharField(max_length=200)
    option2A=models.CharField(max_length=80)
    option2B=models.CharField(max_length=80)
    option2C=models.CharField(max_length=80,blank=True,null=True)
    option2D=models.CharField(max_length=80,blank=True,null=True)
    image2=models.CharField(max_length=600,blank=True,null=True)

    que3=models.CharField(max_length=200)
    option3A=models.CharField(max_length=80)
    option3B=models.CharField(max_length=80)
    option3C=models.CharField(max_length=80,blank=True,null=True)
    option3D=models.CharField(max_length=80,blank=True,null=True)
    image3=models.CharField(max_length=600,blank=True,null=True)

    que4=models.CharField(max_length=200)
    option4A=models.CharField(max_length=80)
    option4B=models.CharField(max_length=80)
    option4C=models.CharField(max_length=80,blank=True,null=True)
    option4D=models.CharField(max_length=80,blank=True,null=True)
    image4=models.CharField(max_length=600,blank=True,null=True)


class YouLookLikeScore(models.Model):
    category=models.CharField(max_length=30)
    code=models.CharField(max_length=4)
    name=models.CharField(max_length=40)
    image=models.CharField(max_length=600)
    text=models.CharField(max_length=200)
