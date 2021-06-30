from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class RfQuestionBank(models.Model):
    que=models.CharField(max_length=200,blank=True,null=True)


class QuizQuestionBank(models.Model):
    part1=models.CharField(max_length=200,blank=True,null=True)
    part2=models.CharField(max_length=200,blank=True,null=True)
    optionA=models.CharField(max_length=50)
    imgA=models.CharField(max_length=500,blank=True,null=True)
    optionB=models.CharField(max_length=50)
    imgB=models.CharField(max_length=500,blank=True,null=True)
    optionC=models.CharField(max_length=50,blank=True,null=True)
    imgC=models.CharField(max_length=500,blank=True,null=True)
    optionD=models.CharField(max_length=50,blank=True,null=True)
    imgD=models.CharField(max_length=500,blank=True,null=True)


class Quiz(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    code=models.CharField(max_length=14,unique=True)
    name=models.CharField(max_length=30)
    # start_date = models.DateTimeField(default=timezone.now)

    que1=models.CharField(max_length=200)
    option1A=models.CharField(max_length=50)
    img1A=models.CharField(max_length=500,blank=True,null=True)
    option1B=models.CharField(max_length=50)
    img1B=models.CharField(max_length=500,blank=True,null=True)
    option1C=models.CharField(max_length=50,blank=True,null=True)
    img1C=models.CharField(max_length=500,blank=True,null=True)
    option1D=models.CharField(max_length=50,blank=True,null=True)
    img1D=models.CharField(max_length=500,blank=True,null=True)
    ans1=models.IntegerField()


    que2=models.CharField(max_length=200)
    option2A=models.CharField(max_length=50)
    img2A=models.CharField(max_length=500,blank=True,null=True)
    option2B=models.CharField(max_length=50)
    img2B=models.CharField(max_length=500,blank=True,null=True)
    option2C=models.CharField(max_length=50,blank=True,null=True)
    img2C=models.CharField(max_length=500,blank=True,null=True)
    option2D=models.CharField(max_length=50,blank=True,null=True)
    img2D=models.CharField(max_length=500,blank=True,null=True)
    ans2=models.IntegerField()


    que3=models.CharField(max_length=200)
    option3A=models.CharField(max_length=50)
    img3A=models.CharField(max_length=500,blank=True,null=True)
    option3B=models.CharField(max_length=50)
    img3B=models.CharField(max_length=500,blank=True,null=True)
    option3C=models.CharField(max_length=50,blank=True,null=True)
    img3C=models.CharField(max_length=500,blank=True,null=True)
    option3D=models.CharField(max_length=50,blank=True,null=True)
    img3D=models.CharField(max_length=500,blank=True,null=True)
    ans3=models.IntegerField()


    que4=models.CharField(max_length=200)
    option4A=models.CharField(max_length=50)
    img4A=models.CharField(max_length=500,blank=True,null=True)
    option4B=models.CharField(max_length=50)
    img4B=models.CharField(max_length=500,blank=True,null=True)
    option4C=models.CharField(max_length=50,blank=True,null=True)
    img4C=models.CharField(max_length=500,blank=True,null=True)
    option4D=models.CharField(max_length=50,blank=True,null=True)
    img4D=models.CharField(max_length=500,blank=True,null=True)
    ans4=models.IntegerField()


    que5=models.CharField(max_length=200)
    option5A=models.CharField(max_length=50)
    img5A=models.CharField(max_length=500,blank=True,null=True)
    option5B=models.CharField(max_length=50)
    img5B=models.CharField(max_length=500,blank=True,null=True)
    option5C=models.CharField(max_length=50,blank=True,null=True)
    img5C=models.CharField(max_length=500,blank=True,null=True)
    option5D=models.CharField(max_length=50,blank=True,null=True)
    img5D=models.CharField(max_length=500,blank=True,null=True)
    ans5=models.IntegerField()


    que6=models.CharField(max_length=200)
    option6A=models.CharField(max_length=50)
    img6A=models.CharField(max_length=500,blank=True,null=True)
    option6B=models.CharField(max_length=50)
    img6B=models.CharField(max_length=500,blank=True,null=True)
    option6C=models.CharField(max_length=50,blank=True,null=True)
    img6C=models.CharField(max_length=500,blank=True,null=True)
    option6D=models.CharField(max_length=50,blank=True,null=True)
    img6D=models.CharField(max_length=500,blank=True,null=True)
    ans6=models.IntegerField()


    que7=models.CharField(max_length=200)
    option7A=models.CharField(max_length=50)
    img7A=models.CharField(max_length=500,blank=True,null=True)
    option7B=models.CharField(max_length=50)
    img7B=models.CharField(max_length=500,blank=True,null=True)
    option7C=models.CharField(max_length=50,blank=True,null=True)
    img7C=models.CharField(max_length=500,blank=True,null=True)
    option7D=models.CharField(max_length=50,blank=True,null=True)
    img7D=models.CharField(max_length=500,blank=True,null=True)
    ans7=models.IntegerField()


    que8=models.CharField(max_length=200)
    option8A=models.CharField(max_length=50)
    img8A=models.CharField(max_length=500,blank=True,null=True)
    option8B=models.CharField(max_length=50)
    img8B=models.CharField(max_length=500,blank=True,null=True)
    option8C=models.CharField(max_length=50,blank=True,null=True)
    img8C=models.CharField(max_length=500,blank=True,null=True)
    option8D=models.CharField(max_length=50,blank=True,null=True)
    img8D=models.CharField(max_length=500,blank=True,null=True)
    ans8=models.IntegerField()


    que9=models.CharField(max_length=200)
    option9A=models.CharField(max_length=50)
    img9A=models.CharField(max_length=500,blank=True,null=True)
    option9B=models.CharField(max_length=50)
    img9B=models.CharField(max_length=500,blank=True,null=True)
    option9C=models.CharField(max_length=50,blank=True,null=True)
    img9C=models.CharField(max_length=500,blank=True,null=True)
    option9D=models.CharField(max_length=50,blank=True,null=True)
    img9D=models.CharField(max_length=500,blank=True,null=True)
    ans9=models.IntegerField()


    que10=models.CharField(max_length=200)
    option10A=models.CharField(max_length=50)
    img10A=models.CharField(max_length=500,blank=True,null=True)
    option10B=models.CharField(max_length=50)
    img10B=models.CharField(max_length=500,blank=True,null=True)
    option10C=models.CharField(max_length=50,blank=True,null=True)
    img10C=models.CharField(max_length=500,blank=True,null=True)
    option10D=models.CharField(max_length=50,blank=True,null=True)
    img10D=models.CharField(max_length=500,blank=True,null=True)
    ans10=models.IntegerField()


class QuizResponse(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quizcode=models.CharField(max_length=14)
    respcode=models.CharField(max_length=14)
    name=models.CharField(max_length=25)

    marks=models.IntegerField()
    ans1=models.IntegerField()
    ans2=models.IntegerField()
    ans3=models.IntegerField()
    ans4=models.IntegerField()
    ans5=models.IntegerField()
    ans6=models.IntegerField()
    ans7=models.IntegerField()
    ans8=models.IntegerField()
    ans9=models.IntegerField()
    ans10=models.IntegerField()

    # one user can ans one quiz only onese
    class Meta:
        unique_together = (('quizcode', 'respcode'),)
        index_together = (('quizcode', 'respcode'),)

