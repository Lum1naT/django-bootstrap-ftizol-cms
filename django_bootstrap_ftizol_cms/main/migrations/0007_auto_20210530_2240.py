# Generated by Django 3.1.7 on 2021-05-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210530_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ft_worker',
            name='social_security_number',
        ),
        migrations.AddField(
            model_name='ft_worker',
            name='password',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Heslo'),
        ),
    ]