from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100,blank=True,null=True)
    vipValidDate=models.DateTimeField(blank=True,null=True)
    # 0 is user,1 is admin
    state=models.IntegerField()


class Film(models.Model):
    name=models.CharField(max_length=100)
    releaseTime=models.DateTimeField()
    downTime=models.DateTimeField()
    timeLength=models.IntegerField()
    price=models.IntegerField()
    screen=models.IntegerField()
    introduction=models.CharField(max_length=100,blank=True,null=True)
    actor=models.CharField(max_length=100,blank=True,null=True)
    state=models.IntegerField(blank=True, null= True)

class ScheduleFilm(models.Model):
    timing=models.CharField(max_length=100,blank=True,null=True)
    monday=models.CharField(max_length=100,blank=True,null=True)
    tuesday=models.CharField(max_length=100,blank=True,null=True)
    wednesday=models.CharField(max_length=100,blank=True,null=True)
    thursday=models.CharField(max_length=100,blank=True,null=True)
    friday=models.CharField(max_length=100,blank=True,null=True)
    saturday=models.CharField(max_length=100,blank=True,null=True)
    sunday=models.CharField(max_length=100,blank=True,null=True)


class Order(models.Model):
    userId=models.IntegerField()
    filmName=models.CharField(max_length=100)
    time=models.DateTimeField()
    price=models.IntegerField()
    screen = models.IntegerField()
    state=models.IntegerField(blank=True,null=True)