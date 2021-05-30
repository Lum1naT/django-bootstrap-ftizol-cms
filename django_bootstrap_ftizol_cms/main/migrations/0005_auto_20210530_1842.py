# Generated by Django 3.1.7 on 2021-05-30 16:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210530_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ft_place',
            options={'ordering': ['name', 'region'], 'verbose_name': 'Místo', 'verbose_name_plural': 'Místa'},
        ),
        migrations.AlterModelOptions(
            name='ft_worker',
            options={'verbose_name': '\nVrtač', 'verbose_name_plural': '\nVratči'},
        ),
        migrations.AlterField(
            model_name='ft_event',
            name='company_worked_with',
            field=models.ManyToManyField(blank=True, related_name='Spolupracující', to='main.ft_Company'),
        ),
        migrations.AlterField(
            model_name='ft_event',
            name='workers',
            field=models.ManyToManyField(blank=True, related_name='Vrtači', to='main.ft_Worker'),
        ),
        migrations.CreateModel(
            name='ft_Upcoming_Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Název akce')),
                ('start_date', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Začátek akce')),
                ('end_date', models.DateField(blank=True, default=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Začátek akce'), null=True, verbose_name='Konec akce')),
                ('description', models.TextField(verbose_name='Popis')),
                ('total_meters', models.FloatField(blank=True, null=True, verbose_name='Metrů čtverečních celkem')),
                ('workers_required', models.IntegerField(blank=True, default=2, verbose_name='Vrtačů potřeba')),
                ('wall_type', models.CharField(choices=[('Cihla', 'Cihla'), ('50/50', '50/50'), ('Kamen', 'Kamen')], default='50/50', max_length=10, verbose_name='Typ zdiva')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.ft_place', verbose_name='Místo')),
                ('workers_ready', models.ManyToManyField(blank=True, related_name='_ft_upcoming_event_workers_ready_+', to='main.ft_Worker')),
            ],
        ),
    ]