# Generated by Django 3.1.7 on 2021-06-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210602_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ft_upcoming_event',
            name='end_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ft_upcoming_event',
            name='end_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ft_upcoming_event',
            name='start_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ft_upcoming_event',
            name='start_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ft_worker',
            name='password',
            field=models.CharField(blank=True, default='qwoo', max_length=15, verbose_name='Heslo'),
        ),
    ]
