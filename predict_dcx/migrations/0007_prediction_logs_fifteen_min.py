# Generated by Django 3.1.7 on 2022-01-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_dcx', '0006_prediction_counter_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction_logs',
            name='fifteen_min',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
