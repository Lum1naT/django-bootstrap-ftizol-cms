# Generated by Django 3.1.7 on 2021-06-02 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210603_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ft_worker',
            name='password',
            field=models.CharField(blank=True, default='oyyz', max_length=15, verbose_name='Heslo'),
        ),
    ]