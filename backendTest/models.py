from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Actions(models.Model):
    actionId = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add = False, null=True)
    type = models.TextField(null=True)
    user = models.ForeignKey(User, related_name = 'actions', on_delete=models.CASCADE,  db_column = "user")

    class Meta:
        verbose_name = "Actions"
        db_table = "Actions"

class Properties(models.Model):
    propertiesId = models.AutoField(primary_key=True)
    pageFrom = models.TextField(null=True)
    pageTo = models.TextField(null=True)
    viewedId = models.TextField(null=True)
    locationX = models.IntegerField(null=True)
    locationY = models.IntegerField(null=True)
    actionId = models.OneToOneField(Actions, on_delete=models.CASCADE, db_column = "actionId")

    class Meta:
        verbose_name = "Properties"
        db_table = "Properties"

class Session(models.Model):

    sessionId = models.TextField(null=True)
    userId = models.ForeignKey(User, related_name = 'session', on_delete=models.CASCADE, db_column = "userId")

    class Meta:
        verbose_name = "Session"
        db_table = "Session"
