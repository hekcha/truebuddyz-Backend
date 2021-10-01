from django.db import models
from django.contrib.auth.models import User

class QuizQuestionBank(models.Model):
    category=models.CharField(max_length=30)
    part1=models.CharField(max_length=200,blank=True,null=True)
    part2=models.CharField(max_length=200,blank=True,null=True)
    optionA=models.CharField(max_length=80)
    optionB=models.CharField(max_length=80)
    optionC=models.CharField(max_length=80,blank=True,null=True)
    optionD=models.CharField(max_length=80,blank=True,null=True)


class Quiz(models.Model):
    category=models.CharField(max_length=30)
    is_active=models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=18)

    que1=models.CharField(max_length=200)
    option1A=models.CharField(max_length=80)
    option1B=models.CharField(max_length=80)
    option1C=models.CharField(max_length=80,blank=True,null=True)
    option1D=models.CharField(max_length=80,blank=True,null=True)
    ans1=models.IntegerField()


    que2=models.CharField(max_length=200)
    option2A=models.CharField(max_length=80)
    option2B=models.CharField(max_length=80)
    option2C=models.CharField(max_length=80,blank=True,null=True)
    option2D=models.CharField(max_length=80,blank=True,null=True)
    ans2=models.IntegerField()


    que3=models.CharField(max_length=200)
    option3A=models.CharField(max_length=80)
    option3B=models.CharField(max_length=80)
    option3C=models.CharField(max_length=80,blank=True,null=True)
    option3D=models.CharField(max_length=80,blank=True,null=True)
    ans3=models.IntegerField()


    que4=models.CharField(max_length=200)
    option4A=models.CharField(max_length=80)
    option4B=models.CharField(max_length=80)
    option4C=models.CharField(max_length=80,blank=True,null=True)
    option4D=models.CharField(max_length=80,blank=True,null=True)
    ans4=models.IntegerField()


    que5=models.CharField(max_length=200)
    option5A=models.CharField(max_length=80)
    option5B=models.CharField(max_length=80)
    option5C=models.CharField(max_length=80,blank=True,null=True)
    option5D=models.CharField(max_length=80,blank=True,null=True)
    ans5=models.IntegerField()


    que6=models.CharField(max_length=200)
    option6A=models.CharField(max_length=80)
    option6B=models.CharField(max_length=80)
    option6C=models.CharField(max_length=80,blank=True,null=True)
    option6D=models.CharField(max_length=80,blank=True,null=True)
    ans6=models.IntegerField()


    que7=models.CharField(max_length=200)
    option7A=models.CharField(max_length=80)
    option7B=models.CharField(max_length=80)
    option7C=models.CharField(max_length=80,blank=True,null=True)
    option7D=models.CharField(max_length=80,blank=True,null=True)
    ans7=models.IntegerField()


    que8=models.CharField(max_length=200)
    option8A=models.CharField(max_length=80)
    option8B=models.CharField(max_length=80)
    option8C=models.CharField(max_length=80,blank=True,null=True)
    option8D=models.CharField(max_length=80,blank=True,null=True)
    ans8=models.IntegerField()


    que9=models.CharField(max_length=200)
    option9A=models.CharField(max_length=80)
    option9B=models.CharField(max_length=80)
    option9C=models.CharField(max_length=80,blank=True,null=True)
    option9D=models.CharField(max_length=80,blank=True,null=True)
    ans9=models.IntegerField()


    que10=models.CharField(max_length=200)
    option10A=models.CharField(max_length=80)
    option10B=models.CharField(max_length=80)
    option10C=models.CharField(max_length=80,blank=True,null=True)
    option10D=models.CharField(max_length=80,blank=True,null=True)
    ans10=models.IntegerField()


class QuizResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quizcode = models.CharField(max_length=14)
    respcode = models.CharField(max_length=14)
    name = models.CharField(max_length=18)

    marks = models.IntegerField()
    ans1 = models.IntegerField()
    ans2 = models.IntegerField()
    ans3 = models.IntegerField()
    ans4 = models.IntegerField()
    ans5 = models.IntegerField()
    ans6 = models.IntegerField()
    ans7 = models.IntegerField()
    ans8 = models.IntegerField()
    ans9 = models.IntegerField()
    ans10 = models.IntegerField()

    # one user can ans one quiz only onese
    class Meta:
        unique_together = (('quizcode', 'respcode'),)
        index_together = (('quizcode', 'respcode'),)
