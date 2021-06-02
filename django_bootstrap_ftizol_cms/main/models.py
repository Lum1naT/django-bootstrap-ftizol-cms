from django.db import models
from django.db.models.deletion import RESTRICT
from django.db.models.enums import Choices
from django.db.models.fields.related import ManyToManyField
from datetime import datetime
import random
import unidecode


class ft_User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(("Email"), max_length=254)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class ft_Place(models.Model):
    REGIONS = [
        ('JČ', 'Jihočeský'),
        ('PLZ', 'Plzeňský'),
        ('KAR', 'Karlovarský'),
        ('LIB', 'Liberecký'),
        ('STŘ', 'Středočeský a Praha'),
        ('KHD', 'Královehradecký'),
        ('JHM', 'Jihomoravský'),
        ('VYS', 'Vysočina'),
        ('ÚST', 'Ústecký'),
        ('PAR', 'Pardubický'),
        ('OLM', 'Olomoucký'),
        ('ZLN', 'Zlínský'),
        ('MSZ', 'Moravskoslezský'),
    ]
    name = models.CharField(("Název města"), max_length=100)
    region = models.CharField(
        ("Kraj"), choices=REGIONS, max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        # Add verbose name
        verbose_name = 'Místo'
        verbose_name_plural = 'Místa'
        ordering = ["name", "region"]


def generate_password():
    result = ""
    result += ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')
                      for _ in range(4))
    return result


class ft_Worker(models.Model):
    GENDERS = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]

    first_name = models.CharField(("Jméno"), max_length=30)
    last_name = models.CharField(("Příjmení"), max_length=30)
    display_name = models.CharField(("Zobrazovací Jméno"), max_length=30)
    gender = models.CharField(
        ("Pohlaví"), max_length=1, choices=GENDERS, default='M')
    email = models.EmailField(("Email"),
                              max_length=254, blank=True, null=True)
    username = models.CharField(
        ("Uživatelské jméno"), max_length=50, null=True, blank=True)
    phone_number = models.CharField(
        ("Telefonní číslo"), max_length=50, blank=True, null=True)
    bank_account_number = models.CharField(
        ("Číslo účtu"), max_length=100, default="cislo/uctu", blank=True)

    # Personal Info
    # TODO: password hashing - this is not a good idea to store passwords like this, i know.
    password = models.CharField(
        ("Heslo"), max_length=15, default=str(generate_password()), blank=True)
    date_of_birth = models.DateField(
        ("Datum narození"), null=True, blank=True, default="2000-01-01")

    power = models.IntegerField(
        ("Síla"), null=True, blank=True, default=10,)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        # Add verbose name
        verbose_name = '\nVrtač'
        verbose_name_plural = '\nVrtači'


class ft_Company(models.Model):
    name = models.CharField(("Jméno"), max_length=100)

    class Meta:
        # Add verbose name
        verbose_name = 'Spolupracující'
        verbose_name_plural = 'Spolupracující'
        ordering = ["name"]

    def __str__(self):
        return self.name


class ft_Event(models.Model):
    name = models.CharField(("Název akce"), max_length=100)
    date = models.DateField(default=datetime.now, blank=True)

    total_meters = models.FloatField(
        ("Metrů čtverečních celkem"), blank=True, null=True)
    czk_per_meter = models.FloatField(("Cena za metr"), blank=True, null=True)
    place = models.ForeignKey(
        ft_Place, on_delete=(models.RESTRICT), verbose_name=("Místo"), blank=True, null=True)
    workers = models.ManyToManyField(
        ft_Worker, ("Vrtači"), blank=True)

    company_worked_with = models.ManyToManyField(
        ft_Company, ("Spolupracující"), blank=True)

    # photos = models.ImageField(upload_to='events', blank=True, null=True)

    class Meta:
        # Add verbose name
        verbose_name = 'Akce'
        verbose_name_plural = 'Akce'
        ordering = ["total_meters", "place", "name"]

    def __str__(self):
        return self.name


class ft_Upcoming_Event(models.Model):
    WALL_TYPES = [
        ('Cihla', 'Cihla'),
        ('50/50', '50/50'),
        ('Kamen', 'Kamen')  # Zde!
    ]

    name = models.CharField(("Název akce"), max_length=100)
    start_date = models.DateField(
        ("Začátek akce"), default=datetime.now, blank=True)
    start_day = models.IntegerField(
        blank=True, null=True, default=0)
    start_month = models.IntegerField(verbose_name=("Měsíc"),
                                      blank=True, null=True, default=0)

    year = models.IntegerField(verbose_name=("Rok"),
                               blank=True, null=True, default=2021)
    end_date = models.DateField(
        ("Konec akce"), default=start_date, blank=True, null=True)

    end_day = models.IntegerField(
        blank=True, null=True, default=0)
    end_month = models.IntegerField(
        blank=True, null=True, default=0)

    description = models.TextField(("Popis"), max_length=250)
    place = models.ForeignKey(
        ft_Place, on_delete=(models.RESTRICT), verbose_name=("Místo"), blank=True, null=True)
    total_meters = models.IntegerField(
        ("Metrů čtverečních celkem"), blank=True, null=True)
    workers_required = models.IntegerField(
        ("Vrtačů potřeba"), blank=True)
    workers_ready = models.ManyToManyField(
        ft_Worker, ("Dostupní vrtači+"), blank=True)
    wall_type = models.CharField(
        ("Typ zdiva"), max_length=10, choices=WALL_TYPES, default='50/50')

    class Meta:
        # Add verbose name
        verbose_name = '\nNadcházející akce'
        verbose_name_plural = '\nNadcházející akce'
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.start_day = self.start_date.day
        self.start_month = self.start_date.month
        self.end_day = self.end_date.day
        self.end_month = self.end_date.month

        self.year = self.start_date.year

        avg_power = 1
        divisor = 0
        for worker in self.workers_ready.all():
            avg_power *= worker.power
            divisor += 1

        meters_per_day = 1
        number_of_days = abs(self.start_day - self.end_day)+1
        if(self.wall_type == 'Kamen'):
            meters_per_day *= 1.2 * avg_power

        elif(self.wall_type == '50/50'):
            meters_per_day *= 1.5 * avg_power

        elif(self.wall_type == 'Cihla'):
            meters_per_day *= 2 * avg_power

        self.workers_required = int((int(self.total_meters) /
                                     (int(meters_per_day * number_of_days))))

        super(ft_Upcoming_Event, self).save(*args, **kwargs)
