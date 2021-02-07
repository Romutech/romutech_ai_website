from django.db import models
from django.utils import timezone

class Home(models.Model):
    logo    = models.ImageField(upload_to='logo')
    picture = models.ImageField(upload_to='picture')
    date    = models.DateTimeField(default=timezone.now)


class Features(models.Model):
    titre       = models.CharField(max_length=200)
    description = models.TextField()
    features    = models.JSONField(null=True)


class Application(models.Model):
    titre   = models.CharField(max_length=200)
    button  = models.CharField(max_length=50)


class Api(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()


class Documentation(models.Model):
    titre       = models.CharField(max_length=200)
    description = models.TextField()
    button      = models.CharField(max_length=50)
    