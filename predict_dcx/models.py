from django.db import models
from django.db.models.deletion import CASCADE
import django_tables2 as tables
from datetime import date, datetime


class prediction(models.Model):
    coin_name = models.CharField(max_length=30,primary_key=True) 

class prediction_logs(models.Model):
    coin_name = models.ForeignKey(prediction,on_delete=CASCADE)
    change_24_hour = models.FloatField(blank=True,null=True)
    high = models.CharField(max_length=50,blank=True,null=True)
    low =  models.CharField(max_length=50,blank=True,null=True)
    bid = models.CharField(max_length=50,blank=True,null=True)
    ask = models.CharField(max_length=50,blank=True,null=True)
    last_price = models.CharField(max_length=50,blank=True,null=True)
    last_price_fifteen = models.CharField(default=0, max_length=50, blank=True,null=True)
    fifteen_min = models.FloatField(default=0, blank=True, null = True)

class prediction_counter(models.Model):
    coin_name = models.ForeignKey(prediction,on_delete=CASCADE)
    latest_price = models.CharField(max_length=50,blank=True,null=True)
    max_price = models.CharField(max_length=50,default=-1)
    cnt = models.IntegerField(default = 0)
    cnt1 = models.IntegerField(default= 0)
    last_updated = models.DateTimeField(auto_now=datetime.now())

class SimpleTable(tables.Table):
    class Meta:
        model = prediction_counter 
        attrs = {"class": "table table-dark table-striped table-hover table-bordered", "id": "myTable"}

class SimpleTable1(tables.Table):
    class Meta:
        model = prediction_logs 
        attrs = {"class": "table table-dark table-striped table-hover table-bordered", "id": "myTable"}