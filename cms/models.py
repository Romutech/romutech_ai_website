from django.db import models
from django.utils import timezone

class Home(models.Model):
    logo = models.ImageField(upload_to='logo')
    picture = models.ImageField(upload_to='picture')
    date = models.DateTimeField(default=timezone.now)
    