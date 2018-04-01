# Generated by Django 2.0.2 on 2018-03-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_match_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
    ]