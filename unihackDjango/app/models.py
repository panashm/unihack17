# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class Organisation(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.name


class Badge(models.Model):
    name = models.CharField(max_length=50)
    organisation = models.ForeignKey(Organisation)
    image = models.ImageField(upload_to='badge_image', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500, default='')

    def __str__(self):
        return "{}: {}".format(self.organisation.name, self.name)

class Consumer(models.Model):
    user = models.OneToOneField(User)
    badge = models.ManyToManyField(Badge)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

class BadgeClaim(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    consumer = models.ForeignKey(Consumer)
    badge = models.ForeignKey(Badge)

    def __str__(self):
        return "{} - {}: {}".format(self.timestamp, self.consumer.user.username, self.badge.name)


class Business(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    badge = models.ManyToManyField(Badge)

    description = models.TextField(max_length=500, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    profileImage = models.ImageField(upload_to='profile_image', blank=True)
    coverPhoto = models.ImageField(upload_to='cover_photo', blank=True)
    address = models.CharField(max_length=100, blank=True)
    lat = models.DecimalField(max_digits=10, decimal_places=7, default=0, blank=True)
    lng = models.DecimalField(max_digits=10, decimal_places=7, default=0, blank=True)


    def __str__(self):
        return self.name
