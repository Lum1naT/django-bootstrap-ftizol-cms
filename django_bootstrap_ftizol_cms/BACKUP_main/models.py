from django.db import models
from django.db.models.deletion import RESTRICT
from django.db.models.fields.related import ManyToManyField


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
    name = models.CharField(verbose_name="Název města", max_length=100)
    region = models.CharField(
        verbose_name="Kraj", choices=REGIONS, max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        # Add verbose name
        verbose_name = 'Místo'
        verbose_name_plural = 'Místa'


class ft_Worker(models.Model):
    GENDERS = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]

    first_name = models.CharField(("Jméno"), max_length=30)
    last_name = models.CharField(("Příjmení"), max_length=30)
    gender = models.CharField(
        ("Pohlaví"), max_length=1, choices=GENDERS, default='M')
    email = models.EmailField(verbose_name="Email",
                              max_length=254, blank=True, null=True)
    username = models.CharField(
        ("Uživatelské jméno"), max_length=50, null=True, blank=True)
    phone_number = models.CharField(
        ("Telefonní číslo"), max_length=50, blank=True, null=True)
    bank_account_number = models.CharField(
        ("Číslo účtu"), max_length=100, default="123456/9999", blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        # Add verbose name
        verbose_name = 'Vrtač'
        verbose_name_plural = 'Vratči'


class ft_Company(models.Model):
    name = models.CharField(("Jméno"), max_length=100)

    class Meta:
        # Add verbose name
        verbose_name = 'Spolupracující'
        verbose_name_plural = 'Spolupracující'

    def __str__(self):
        return self.name


class ft_Event(models.Model):
    name = models.CharField(("Název akce"), max_length=100)

    total_meters = models.FloatField(
        ("Metrů čtverečních celkem"), blank=True, null=True)
    czk_per_meter = models.FloatField(("Cena za metr"), blank=True, null=True)
    place = models.ForeignKey(
        ft_Place, on_delete=(models.RESTRICT), verbose_name=("Místo"), blank=True, null=True)
    workers = models.ManyToManyField(
        ft_Worker, verbose_name=("Vrtači"), blank=True)

    company_worked_with = models.ManyToManyField(
        ft_Company, verbose_name=("Spolupracující"), blank=True)

    photos = models.ImageField(upload_to='events', blank=True, null=True)

    class Meta:
        # Add verbose name
        verbose_name = 'Akce'
        verbose_name_plural = 'Akce'

    def __str__(self):
        return self.name
