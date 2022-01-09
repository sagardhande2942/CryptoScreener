from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from predict_dcx.helper import pred_cal,save_to_model,predict_bid_logic
from predict_dcx.models import prediction, prediction_counter,prediction_logs, SimpleTable
import json2table
from django.template import RequestContext
import json
import pandas as pd


def predict(request):     
    prediction_counter_objects = prediction_counter.objects.all()
    sorted_objects = prediction_counter_objects.order_by('cnt')
    sorted_objects = sorted_objects[::-1]
    table = SimpleTable(sorted_objects) 
    return render(request, "table.html", {"table": table})


def predict1(request):    
    prediction_counter_objects = prediction_counter.objects.all()
    sorted_objects = prediction_counter_objects.order_by('cnt1')
    sorted_objects = sorted_objects[::-1]
    table = SimpleTable(sorted_objects)
    return render(request, "table1.html", {"table": table})
    


def delete(request):
    if request.method == "POST":
        print("hii")
        myCode = int(request.POST.get("code", ""))
        if myCode == 2942:
            records = prediction_counter.objects.all()
            records.delete()
            return render(request, "succesfull.html")
        else:   
            return render(request, "unsuccessfull.html")
    else:
        print("hii")
        return render(request, "delete.html")


def getLowRsi(request):
    pass

def predict_bid(request):
    predict_bid_logic()


