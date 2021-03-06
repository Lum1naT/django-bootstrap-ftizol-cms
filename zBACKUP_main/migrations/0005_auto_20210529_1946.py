# Generated by Django 3.1.7 on 2021-05-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210529_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='ft_event',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='events'),
        ),
        migrations.AlterField(
            model_name='ft_event',
            name='czk_per_meter',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena za metr'),
        ),
        migrations.AlterField(
            model_name='ft_worker',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefonní číslo'),
        ),
    ]
