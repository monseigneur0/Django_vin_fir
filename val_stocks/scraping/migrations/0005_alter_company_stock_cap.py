# Generated by Django 3.2.9 on 2022-01-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_company_stock_cap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='stock_cap',
            field=models.TextField(null=True, verbose_name='시가 총액'),
        ),
    ]
