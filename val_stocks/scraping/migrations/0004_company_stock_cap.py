# Generated by Django 3.2.9 on 2022-01-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_alter_daily_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='stock_cap',
            field=models.IntegerField(null=True, verbose_name='시가 총액'),
        ),
    ]
