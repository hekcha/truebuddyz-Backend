from django.db import models

# Create your models here.
class RfQuestionBank(models.Model):
    category=models.CharField(max_length=20)
    que=models.CharField(max_length=200,blank=True,null=True)

