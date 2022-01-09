import requests
from predict_dcx.models import prediction,prediction_logs, prediction_counter
import time
import threading
from datetime import datetime

def pred_cal():
    url = "https://api.coindcx.com/exchange/ticker"
    try:
        response = requests.get(url)
    except:
        time.sleep(20)
        pred_cal()
    data = response.json()
    a = []
    for i in data:
        if str(i['market']).endswith('BTC'):
            a.append(i)
    return a

def pred_cal1():
    change_dict = []
    change_list = pred_cal()
    for i in change_list:
        # prediction.objects.create(coin_name= i['market'])
        save_to_model(i)

def save_to_model(i):
    pred = prediction.objects.filter(coin_name =i['market']).first()
    new_dict = {
        'coin_name':pred,
        'change_24_hour':i['change_24_hour'],
        'bid':i['bid'],
        'ask':i['ask'],
        'high':i['high'],
        'low':i['low'],
        'last_price':i['last_price']
    }
    latest_obj1 = prediction_logs.objects.filter(coin_name = pred)
    latest_obj = latest_obj1.first()
    if latest_obj == None:
        prediction_logs(**new_dict).save()
    else:
        latest_obj1.update(**new_dict)

def predict_bid_logic():
    while True:
        print('start')
        pred_cal1()
        time.sleep(60)
        print('end')
        coins = prediction.objects.all()
        for i in coins:
            my_instance = prediction.objects.filter(coin_name = i.coin_name).first()
            pred = prediction_logs.objects.filter(coin_name = my_instance).first()
            store_updates(pred, my_instance)


def store_updates(pred, coin):
    latest_price = pred.last_price
    last_object1 = prediction_counter.objects.filter(coin_name = coin)
    last_object = last_object1.first()
    if last_object == None:
        prediction_counter(coin_name = coin, latest_price = pred.last_price, max_price = pred.last_price).save()
    else:
        max_price = last_object.max_price
        cnt = last_object.cnt
        cnt1 = last_object.cnt1
        
        if latest_price > max_price:
            cnt += 1
            max_price = latest_price
            cnt1 += 1
            last_object1.update(cnt = cnt, cnt1 = cnt1, max_price = max_price, latest_price = latest_price, last_updated = datetime.now())


        if latest_price < max_price:
            cnt -= 1
            last_object1.update(cnt = cnt, cnt1 = cnt1, max_price = max_price, latest_price = latest_price)
        
        last_object1.update(latest_price = latest_price)

        
# def prediction_calcutions(pred):
#     per_cnt = 0
#     per_bid = 0
#     per_ask = 0
#     change_per = {
#         'percent':[],
#         'bid':[],
#         'ask':[]
#     }
#     for v in pred:
#         change_per['percent'].append(v.change_24_hour)
#         change_per['bid'].append(v.bid)
#         change_per['ask'].append(v.ask)

 


timer = threading.Thread(target=predict_bid_logic)
timer.daemon = True
timer.start() 
threading.Thread.__init__.daemon = True