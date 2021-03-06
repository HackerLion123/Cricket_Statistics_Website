# Generated by Django 2.0.2 on 2018-03-26 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_player_runs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='player1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player10',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player11',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player5',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player6',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player7',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player8',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player9',
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Team'),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player1',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player10',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player11',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player4',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player5',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player6',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player7',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player8',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batting_log',
            name='player9',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='bowling_log',
            name='player1',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='bowling_log',
            name='player2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='bowling_log',
            name='player3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='bowling_log',
            name='player4',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='bowling_log',
            name='player5',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
