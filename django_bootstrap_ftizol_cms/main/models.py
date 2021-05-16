from django.db import models
from places.fields import PlacesField


class ft_MyLocationModel(models.Model):
    location = PlacesField()

class ft_User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField((""), max_length=254)
    username = models.CharField(max_length=50)



class ft_Worker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField((""), max_length=254)
    username = models.CharField(max_length=50)


class ft_Event(models.Model):
        name = models.CharField((""), max_length=100)
        date_created = models.DateTimeField((""), auto_now=False, auto_now_add=True)
        created_by = models.ForeignKey(ft_User, verbose_name=(""), on_delete=models.CASCADE)
        last_edited = models.DateTimeField((""), auto_now=True)
        date_created = models.DateTimeField((""), auto_now=False, auto_now_add=True)
        total_meters = models.FloatField((""))
        workers = models.ManyToManyField(ft_Worker, verbose_name=(""))
        location = models.ForeignKey(ft_MyLocationModel, verbose_name=(""), on_delete=models.CASCADE)

