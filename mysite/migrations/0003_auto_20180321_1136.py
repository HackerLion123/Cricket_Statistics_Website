# Generated by Django 2.0.2 on 2018-03-21 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20180321_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='batting2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batting2', to='mysite.Batting_log'),
        ),
        migrations.AlterField(
            model_name='match',
            name='batting1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batting1', to='mysite.Batting_log'),
        ),
    ]