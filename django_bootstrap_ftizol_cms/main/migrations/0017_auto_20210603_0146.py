# Generated by Django 3.1.7 on 2021-06-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210603_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ft_worker',
            name='date_of_birth',
            field=models.DateField(blank=True, default='2000-01-01', null=True, verbose_name='Datum narození'),
        ),
        migrations.AlterField(
            model_name='ft_worker',
            name='password',
            field=models.CharField(blank=True, default='urlm', max_length=15, verbose_name='Heslo'),
        ),
        migrations.AlterField(
            model_name='ft_worker',
            name='power',
            field=models.IntegerField(blank=True, default=10, null=True, verbose_name='Síla'),
        ),
    ]
