from django.contrib.auth.models import User
from django.db import models


class Website(models.Model):
    url = models.URLField()
    users = models.ManyToManyField(User)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    nickname = models.CharField(blank=True, null=True, max_length=50)
    location = models.CharField(blank=True, null=True, max_length=50)
    weight = models.DecimalField(null=True, max_digits=5, decimal_places=2)
