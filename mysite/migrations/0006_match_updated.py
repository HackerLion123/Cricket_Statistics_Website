# Generated by Django 2.0.2 on 2018-03-23 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20180322_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]