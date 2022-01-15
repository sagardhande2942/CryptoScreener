from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from predict_dcx.helper import pred_cal,save_to_model,predict_bid_logic
from predict_dcx.models import SimpleTable1, prediction, prediction_counter,prediction_logs, SimpleTable
import json2table
from django.template import RequestContext
import json
import pandas as pd
import threading
import time
from .telbot import TelNotificaion

def fifteenMin():
    print('15 min')
    prediction_logs_object = prediction_logs.objects.all()
    myString = "Long\n"
    myString1 = "Short\n"
    myString += "|    Name    |    Price    |    15m   |\n"
    myString1 += "|    Name    |    Price    |    15m   |\n"
    check = False
    check1 = False
    for i in prediction_logs_object:
        cur_price = i.last_price
        last_price = i.last_price_fifteen
        if float(last_price) == 0:
            last_price = 1
        if float(cur_price) < float(last_price):
            percent_diff = ((float(last_price) - float(cur_price))/float(cur_price)) * 100
            percent_diff = -1 * percent_diff
            # print("Difference in percentage is : {}%".format(percent_diff))
        else:
            percent_diff = ((float(cur_price) - float(last_price))/float(last_price)) * 100
            # print("Difference in percentage is : {}%".format(percent_diff))
        percent_diff = round(float(percent_diff), 2)
        d = i.__dict__

        if percent_diff > 0.5:
            # for j, k in d.items():
            #     myString += "|"
            #     myString += f"{j} - {k}"
            #     myString += '|\n'
            coin_name1 = d['coin_name_id'].replace('USDT', '')
            check = True
            myString += "    "
            myString += f"{coin_name1}        "
            myString += f"{round(float(d['last_price']), 2)}        "
            myString += f"{percent_diff}        "
            myString += '    \n'
        
        if percent_diff < -0.5:
            coin_name1 = d['coin_name_id'].replace('USDT', '')
            check1 = True
            myString1 += "    "
            myString1 += f"{coin_name1}        "
            myString1 += f"{round(float(d['last_price']), 2)}        "
            myString1 += f"{percent_diff}        "
            myString1 += '    \n'

        

        obj = prediction.objects.filter(coin_name = i.coin_name.coin_name).first()
        a = prediction_logs.objects.filter(coin_name = obj)
        a.update(last_price_fifteen = cur_price, fifteen_min = percent_diff)
    myString += "\n"
    print(myString)
    if check:
        oj = TelNotificaion()
        oj.notify_ending(myString)
    if check1:
        oj = TelNotificaion()
        oj.notify_ending(myString1)

def initiateCountdown():
    time.sleep(1 * 60)
    fifteenMin()
    initiateCountdown()

timer = threading.Thread(target=initiateCountdown)
timer.daemon = True
timer.start() 
threading.Thread.__init__.daemon = True

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
    
def predict2(request):
    prediction_logs_objects = prediction_logs.objects.all()
    sorted_objects = prediction_logs_objects.order_by('fifteen_min')
    sorted_objects = sorted_objects[::-1]
    table = SimpleTable1(sorted_objects)
    return render(request, "table2.html", {"table":table})

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


