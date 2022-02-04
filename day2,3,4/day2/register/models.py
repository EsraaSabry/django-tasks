from django.db import models

# Create your models here.
class myuser(models.Model):
    username=models.CharField(max_length=10)
    firstname =models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.EmailField(max_length =20)
    password=models.CharField(max_length=20)

class students(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    track=models.CharField(max_length=20)



class Intake(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=20)
    sdate =models.DateField()
    edate =models.DateField()

class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)