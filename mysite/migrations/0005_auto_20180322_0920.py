# Generated by Django 2.0.2 on 2018-03-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20180321_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='maiden',
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player11',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bowling_log',
            name='player2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bowling_log',
            name='player3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bowling_log',
            name='player4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bowling_log',
            name='player5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='HighScore',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='average',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='economy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='fours',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='matchplayed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='overs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='run_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='sixs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='wicket_streak',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='wickets',
            field=models.IntegerField(null=True),
        ),
    ]
