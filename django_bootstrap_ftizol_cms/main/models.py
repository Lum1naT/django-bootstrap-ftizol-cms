from django.db import models
from places.fields import PlacesField


class MyLocationModel(models.Model):
    location = PlacesField()

class ft_User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(_(""), max_length=254)
    username = models.CharField(max_length=50)

class ft_Event(models.Model):
        name = models.CharField(_(""), max_length=100)
        date_created = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
        created_by = models.ForeignKey("app.ft_User", verbose_name=_(""), on_delete=models.CASCADE)
        last_edited = models.DateTimeField(_(""), auto_now=True, auto_now_add=True)
        last_edited_by = models.ForeignKey("app.ft_User", verbose_name=_(""), on_delete=models.CASCADE)
        date_created = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
        total_meters = models.FloatField(_(""))
        workers = models.ManyToManyField("app.Worker", verbose_name=_(""))
        location = models.ForeignKey("app.MyLocationModel", verbose_name=_(""), on_delete=models.CASCADE)

class ft_Worker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(_(""), max_length=254)
    username = models.CharField(max_length=50)

