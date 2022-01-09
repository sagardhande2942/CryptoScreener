from django.contrib import admin
from predict_dcx.models import prediction,prediction_logs,prediction_counter

admin.site.register(prediction)
admin.site.register(prediction_logs)
admin.site.register(prediction_counter)
