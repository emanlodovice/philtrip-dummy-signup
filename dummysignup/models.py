from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='profile')
    birthday = models.DateField(null=True)
    location = models.CharField(max_length=225, blank=True)
    work = models.TextField(blank=True)
    beach = models.BooleanField(default=False)
    nature = models.BooleanField(default=False)
    shopping = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
