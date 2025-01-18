from django.db import models

# Create your models here.
class templist(models.Model):
    date = models.CharField(max_length=20)  
    name = models.CharField(max_length=50)  
    department_name = models.CharField(max_length=30)  
    month = models.CharField(max_length=20)  
    amount = models.IntegerField()
    note = models.TextField() 

class currencystate(models.Model):
    id = models.AutoField(primary_key=True) 
    fivehundred = models.IntegerField(default=0)
    twohundred = models.IntegerField(default=0)
    onehundred = models.IntegerField(default=0)
    fifty = models.IntegerField(default=0)
    twenty = models.IntegerField(default=0)
    ten = models.IntegerField(default=0)
    five = models.IntegerField(default=0)
    two = models.IntegerField(default=0)
    one = models.IntegerField(default=0)