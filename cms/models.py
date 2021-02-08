from django.db import models
from django.utils import timezone


class Features(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    features = models.JSONField(null=True)

    class Meta:
        verbose_name = "features"


class Application(models.Model):
    title = models.CharField(max_length=200)
    button = models.CharField(max_length=50)

    class Meta:
        verbose_name = "application"


class Api(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "api"


class Documentation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    button = models.CharField(max_length=50)

    class Meta:
        verbose_name = "documentation"


class Footer(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = "footer"
