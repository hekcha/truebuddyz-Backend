from django.db import models

class RfQuestionBank(models.Model):
    category=models.CharField(max_length=30)
    que=models.CharField(max_length=200,blank=True,null=True)

class RfRoomDetail(models.Model):
    category=models.CharField(max_length=30)
    roomId=models.CharField(max_length=20)
    playerId=models.CharField(max_length=20)
    playerName=models.CharField(max_length=20)

    # The fields roomId, playerId must make a unique set.
    class Meta:
        unique_together = (('roomId', 'playerId'),)
        index_together = (('roomId', 'playerId'),)
