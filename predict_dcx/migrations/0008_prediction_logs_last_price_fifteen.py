# Generated by Django 3.1.7 on 2022-01-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_dcx', '0007_prediction_logs_fifteen_min'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction_logs',
            name='last_price_fifteen',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
    ]