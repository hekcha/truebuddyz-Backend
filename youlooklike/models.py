from django.db import models


class YouLookLikeRandom(models.Model):
    category=models.CharField(max_length=20)
    
    que=models.CharField(max_length=200)
    optionA=models.CharField(max_length=50)
    optionB=models.CharField(max_length=50)
    optionC=models.CharField(max_length=50,blank=True,null=True)
    optionD=models.CharField(max_length=50,blank=True,null=True)
    image=models.CharField(max_length=800,blank=True,null=True)

class YouLookLike(models.Model):
    category=models.CharField(max_length=20)
    
    que1=models.CharField(max_length=200)
    option1A=models.CharField(max_length=50)
    option1B=models.CharField(max_length=50)
    option1C=models.CharField(max_length=50,blank=True,null=True)
    option1D=models.CharField(max_length=50,blank=True,null=True)
    image1=models.CharField(max_length=800,blank=True,null=True)

    que2=models.CharField(max_length=200)
    option2A=models.CharField(max_length=50)
    option2B=models.CharField(max_length=50)
    option2C=models.CharField(max_length=50,blank=True,null=True)
    option2D=models.CharField(max_length=50,blank=True,null=True)
    image2=models.CharField(max_length=800,blank=True,null=True)

    que3=models.CharField(max_length=200)
    option3A=models.CharField(max_length=50)
    option3B=models.CharField(max_length=50)
    option3C=models.CharField(max_length=50,blank=True,null=True)
    option3D=models.CharField(max_length=50,blank=True,null=True)
    image3=models.CharField(max_length=800,blank=True,null=True)

    que4=models.CharField(max_length=200)
    option4A=models.CharField(max_length=50)
    option4B=models.CharField(max_length=50)
    option4C=models.CharField(max_length=50,blank=True,null=True)
    option4D=models.CharField(max_length=50,blank=True,null=True)
    image4=models.CharField(max_length=800,blank=True,null=True)


class YouLookLikeScore(models.Model):
    category=models.CharField(max_length=20)
    code=models.CharField(max_length=4)
    image=models.CharField(max_length=500)
    text=models.CharField(max_length=200)
