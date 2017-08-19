# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Consumer(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class Organisation(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Badge(models.Model):
    name = models.CharField(max_length=50)
    organisation = models.ForeignKey(Organisation)

    def __str__(self):
        return self.name


class Business(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    badge = models.ManyToManyField(Badge)

    def __str__(self):
        return self.name
