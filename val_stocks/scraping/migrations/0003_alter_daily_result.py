# Generated by Django 3.2.9 on 2022-01-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_daily'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='result',
            field=models.TextField(),
        ),
    ]