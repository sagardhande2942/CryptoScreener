from django.urls import path,include
from .views import *
urlpatterns=[
    path('predict/', predict,name='predict'),
    path('predict1/', predict1),
    path('predict_bid/', predict_bid),
    path('delete/', delete),
    path('showrsi/', getLowRsi),
]