# Generated by Django 3.1.7 on 2021-05-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ft_event',
            name='czk_per_meter',
            field=models.FloatField(default=130, verbose_name='Cena za metr'),
            preserve_default=False,
        ),
    ]